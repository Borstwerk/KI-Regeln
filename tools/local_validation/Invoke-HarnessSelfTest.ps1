[CmdletBinding()]
param(
    [string]$BaseRef = 'HEAD',
    [switch]$KeepWorktree
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$env:PYTHONDONTWRITEBYTECODE = '1'

$RepoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$StateRoot = Join-Path $RepoRoot '.validation'
$SelfTestRoot = Join-Path $StateRoot 'selftest'
$SharedState = Join-Path $SelfTestRoot 'shared-state'
$BootstrapState = Join-Path $SelfTestRoot 'bootstrap-state'
$Worktree = Join-Path $SelfTestRoot 'worktree'
$PowerShellExe = (Get-Process -Id $PID).Path
$Results = New-Object System.Collections.ArrayList

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text)
    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Text, (New-Object System.Text.UTF8Encoding($false)))
}

function Reset-Fixture {
    & git.exe -C $Worktree reset --hard HEAD | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'git reset failed in self-test worktree' }
    & git.exe -C $Worktree clean -fd | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'git clean failed in self-test worktree' }
}

function Get-LatestReport {
    param([string]$ValidationState)
    $path = Join-Path $ValidationState 'latest.json'
    if (-not (Test-Path -LiteralPath $path)) { return $null }
    return (Get-Content -Raw -LiteralPath $path | ConvertFrom-Json)
}

function Invoke-FixtureValidation {
    param(
        [string]$ValidationState,
        [string[]]$HarnessArguments
    )
    $old = $env:KI_REGELN_VALIDATION_STATE_DIR
    $env:KI_REGELN_VALIDATION_STATE_DIR = $ValidationState
    try {
        $log = Join-Path $SelfTestRoot ("case-process-{0}.log" -f ([guid]::NewGuid().ToString('N')))
        $args = @('-NoLogo', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', (Join-Path $Worktree 'Validate-KI-Regeln.ps1'))
        $args += $HarnessArguments
        & $PowerShellExe @args *> $log
        $exitCode = $LASTEXITCODE
        $report = Get-LatestReport -ValidationState $ValidationState
        return [pscustomobject]@{ ExitCode = $exitCode; Report = $report; Log = $log }
    } finally {
        $env:KI_REGELN_VALIDATION_STATE_DIR = $old
    }
}

function Has-Code {
    param($Report, [string]$Code)
    if (-not $Report) { return $false }
    return (@($Report.findings | Where-Object { $_.code -eq $Code }).Count -gt 0)
}

function Add-Result {
    param([int]$Number, [string]$Name, [bool]$Passed, [string]$Details)
    [void]$Results.Add([ordered]@{
        case = $Number
        name = $Name
        status = $(if ($Passed) { 'PASS' } else { 'FAIL' })
        details = $Details
    })
    Write-Host ("[{0}] {1,-48} {2}" -f $Number, $Name, $(if ($Passed) { 'PASS' } else { 'FAIL' }))
    if (-not $Passed) { Write-Host ("    {0}" -f $Details) }
}

function Replace-FileText {
    param([string]$RelativePath, [string]$Pattern, [string]$Replacement, [System.Text.RegularExpressions.RegexOptions]$Options = [System.Text.RegularExpressions.RegexOptions]::None)
    $path = Join-Path $Worktree $RelativePath
    $text = [System.IO.File]::ReadAllText($path)
    $regex = New-Object System.Text.RegularExpressions.Regex($Pattern, $Options)
    $updated = $regex.Replace($text, $Replacement, 1)
    if ($updated -eq $text) { throw ("Fixture mutation did not match: {0}" -f $RelativePath) }
    Write-Utf8NoBom -Path $path -Text $updated
}

New-Item -ItemType Directory -Force -Path $SelfTestRoot | Out-Null
if (Test-Path -LiteralPath $Worktree) {
    & git.exe -C $RepoRoot worktree remove --force $Worktree 2>$null | Out-Null
}
& git.exe -C $RepoRoot worktree add --detach $Worktree $BaseRef | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'Unable to create temporary self-test worktree.' }

try {
    $parserScripts = @(
        (Join-Path $Worktree 'Validate-KI-Regeln.ps1'),
        (Join-Path $Worktree 'Validate-KI-Regeln.Core.ps1')
    )
    foreach ($harnessScript in $parserScripts) {
        $parserTokens = $null
        $parserErrors = $null
        [void][System.Management.Automation.Language.Parser]::ParseFile($harnessScript, [ref]$parserTokens, [ref]$parserErrors)
        $scriptName = Split-Path -Leaf $harnessScript
        if (@($parserErrors).Count -gt 0) {
            Write-Host ("[PARSER] {0} FAIL" -f $scriptName)
            foreach ($parserError in @($parserErrors)) {
                Write-Host ("    line {0}, column {1}: {2}" -f $parserError.Extent.StartLineNumber, $parserError.Extent.StartColumnNumber, $parserError.Message)
            }
            throw ("PowerShell parser preflight failed for {0}; controlled self-tests were not started." -f $scriptName)
        }
        Write-Host ("[PARSER] {0} PASS" -f $scriptName)
    }

    # 1. Clean baseline. This exercises the default Full mode and the real eval_coverage_audit.py output contract.
    Reset-Fixture
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @()

    $coveragePython = Join-Path $SharedState 'runtime/venv/Scripts/python.exe'
    $coverageAudit = Join-Path $Worktree 'tools/eval_coverage_audit.py'
    if (-not (Test-Path -LiteralPath $coveragePython)) { throw 'Coverage contract regression requires the bootstrapped portable Python runtime.' }
    $coverageRaw = & $coveragePython $coverageAudit
    if ($LASTEXITCODE -ne 0) { throw 'Direct eval_coverage_audit.py contract probe failed.' }
    $coverageData = (($coverageRaw | Out-String) | ConvertFrom-Json)
    $expectedCoverageFields = @(
        'skill_count',
        'eval_file_count',
        'case_count',
        'coverage_counts',
        'skills_without_evals',
        'one_sided_signal_count',
        'skills',
        'notes'
    )
    $coverageFields = @($coverageData.PSObject.Properties.Name)
    $coverageMissing = @($expectedCoverageFields | Where-Object { $_ -notin $coverageFields })
    $reportCountFields = @($r.Report.counts.PSObject.Properties.Name)
    $coverageContractOk = (
        $coverageMissing.Count -eq 0 -and
        'heuristic_audit_signals' -in $reportCountFields -and
        [int]$r.Report.counts.heuristic_audit_signals -eq [int]$coverageData.one_sided_signal_count
    )

    $historyTestLog = Join-Path $SelfTestRoot 'history-exposure-unit-tests.log'
    Push-Location $Worktree
    try {
        & $coveragePython -m unittest -v tests.test_history_exposure_scan *> $historyTestLog
        $historyTestExit = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    if ($historyTestExit -ne 0) {
        Write-Host '[HISTORY TESTS] FAIL'
        Get-Content -LiteralPath $historyTestLog | ForEach-Object { Write-Host $_ }
        throw 'History exposure regression tests failed; controlled self-tests were stopped.'
    }
    Write-Host '[HISTORY TESTS] PASS'

    $baselineStatus = & git.exe -C $Worktree status --porcelain
    if ($LASTEXITCODE -ne 0) { throw 'Unable to verify clean self-test worktree after baseline validation.' }
    $baselineDirty = (($baselineStatus | Out-String).Trim())
    $worktreeClean = -not [bool]$baselineDirty

    $case1Ok = ($r.ExitCode -eq 0 -and $r.Report.overall -eq 'PASS' -and $r.Report.mode -eq 'Full' -and $coverageContractOk -and $worktreeClean)
    Add-Result 1 'clean current repository' $case1Ok ("exit={0}; mode={1}; missing-contract-fields={2}; heuristic-signals={3}; worktree-clean={4}" -f $r.ExitCode, $r.Report.mode, ($coverageMissing -join ','), $r.Report.counts.heuristic_audit_signals, $worktreeClean)

    # 2. Invalid skill ID / catalog identity mismatch.
    Reset-Fixture
    Replace-FileText 'skill-catalog.yml' '\{id: reflektierender-dialog,' '{id: INVALID_ID,'
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 2 'invalid skill ID' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'SKILL_NAME')) ("exit={0}" -f $r.ExitCode)

    # 3. Missing eval path for a catalogued partial-coverage skill.
    Reset-Fixture
    $evalPath = Join-Path $Worktree 'Evals/Agentenarbeit/context-engineering/cases.yml'
    if (-not (Test-Path -LiteralPath $evalPath)) { throw 'Expected context-engineering eval fixture is missing.' }
    Remove-Item -Force -LiteralPath $evalPath
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 3 'missing eval path' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'EVAL_PATH')) ("exit={0}" -f $r.ExitCode)

    # 4. Wrong coverage: cases exist, catalog says none.
    Reset-Fixture
    Replace-FileText 'skill-catalog.yml' '(\{id: context-engineering,[^\r\n]*?eval_coverage:\s*)partial' '${1}none'
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 4 'wrong eval coverage' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'EVAL_COVERAGE')) ("exit={0}" -f $r.ExitCode)

    # 5. Invalid YAML.
    Reset-Fixture
    $catalog = Join-Path $Worktree 'skill-catalog.yml'
    [System.IO.File]::AppendAllText($catalog, "`n: [validation-broken`n", (New-Object System.Text.UTF8Encoding($false)))
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 5 'invalid YAML' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'YAML')) ("exit={0}" -f $r.ExitCode)

    # 6. Remove a provenance record that only uses aliases; keep the anchor-defining first record intact.
    Reset-Fixture
    $options = [System.Text.RegularExpressions.RegexOptions]::Multiline -bor [System.Text.RegularExpressions.RegexOptions]::Singleline
    Replace-FileText 'Dokumentation/upstream-provenance.yml' '^- source_id: agent-skills-specification\r?\n.*?(?=^- source_id:)' '' $options
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 6 'missing provenance entry' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'PROVENANCE_MISSING')) ("exit={0}" -f $r.ExitCode)

    # 7. Broken local_impact path.
    Reset-Fixture
    Replace-FileText 'Dokumentation/upstream-sources.yml' 'Grundlagen/Mensch-KI-Interaktion\.md' '__validation_missing__/file.md'
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Quick')
    Add-Result 7 'wrong local_impact' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'UPSTREAM_IMPACT')) ("exit={0}" -f $r.ExitCode)

    # 8. Current-tree synthetic exposure. Build the detector-shaped value only at runtime.
    Reset-Fixture
    $secretFixture = Join-Path $Worktree '__validation_exposure_fixture.txt'
    $tokenPrefix = 'gh' + 'p_'
    $tokenBody = '1234567890' + 'ABCDEFGHIJKLMNOPQRST'
    Write-Utf8NoBom -Path $secretFixture -Text ("synthetic={0}{1}{2}" -f $tokenPrefix, $tokenBody, [Environment]::NewLine)
    & git.exe -C $Worktree add '__validation_exposure_fixture.txt' | Out-Null
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Release')
    Add-Result 8 'synthetic exposure finding' ($r.ExitCode -eq 1 -and (Has-Code $r.Report 'EXPOSURE_GITHUB_TOKEN')) ("exit={0}" -f $r.ExitCode)

    # 9. Warning-only case: build the detector-shaped mail value only at runtime.
    Reset-Fixture
    $warningFixture = Join-Path $Worktree '__validation_warning_fixture.txt'
    $mailLocal = 'qa-validation'
    $mailSeparator = [char]64
    $mailDomain = 'example' + '.com'
    Write-Utf8NoBom -Path $warningFixture -Text ("synthetic-contact={0}{1}{2}{3}" -f $mailLocal, $mailSeparator, $mailDomain, [Environment]::NewLine)
    & git.exe -C $Worktree add '__validation_warning_fixture.txt' | Out-Null
    $r = Invoke-FixtureValidation -ValidationState $SharedState -HarnessArguments @('-Release')
    $warningFound = (Has-Code $r.Report 'CONTEXT_EMAIL_ADDRESS')
    Add-Result 9 'warning without error' ($r.ExitCode -eq 0 -and $warningFound) ("exit={0}" -f $r.ExitCode)

    # 10. Missing runtime must fail cleanly with -NoBootstrap, then an isolated first bootstrap must succeed.
    Reset-Fixture
    if (Test-Path -LiteralPath $BootstrapState) { Remove-Item -Recurse -Force -LiteralPath $BootstrapState }
    New-Item -ItemType Directory -Force -Path $BootstrapState | Out-Null
    $missing = Invoke-FixtureValidation -ValidationState $BootstrapState -HarnessArguments @('-Quick','-NoBootstrap')
    $missingOk = ($missing.ExitCode -eq 2 -and (Has-Code $missing.Report 'RUNTIME_MISSING'))

    $sharedDownload = Join-Path $SharedState 'runtime/downloads'
    $bootstrapDownload = Join-Path $BootstrapState 'runtime/downloads'
    if (Test-Path -LiteralPath $sharedDownload) {
        New-Item -ItemType Directory -Force -Path $bootstrapDownload | Out-Null
        Copy-Item -Path (Join-Path $sharedDownload '*') -Destination $bootstrapDownload -Force
    }
    $boot = Invoke-FixtureValidation -ValidationState $BootstrapState -HarnessArguments @('-Quick')
    $bootstrapOk = ($boot.ExitCode -eq 0 -and $boot.Report.runtime.bootstrap_performed -eq $true)
    Add-Result 10 'missing runtime / first bootstrap' ($missingOk -and $bootstrapOk) ("missing-exit={0}; bootstrap-exit={1}" -f $missing.ExitCode, $boot.ExitCode)
} finally {
    if (-not $KeepWorktree) {
        & git.exe -C $RepoRoot worktree remove --force $Worktree 2>$null | Out-Null
    }
}

$failed = @($Results | Where-Object { $_.status -eq 'FAIL' }).Count
$summary = [ordered]@{
    schema_version = 1
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    base_ref = $BaseRef
    passed = $Results.Count - $failed
    failed = $failed
    cases = $Results
}
Write-Utf8NoBom -Path (Join-Path $StateRoot 'selftest-latest.json') -Text (($summary | ConvertTo-Json -Depth 8) + "`n")

Write-Host ''
Write-Host ("Self-tests: {0}/{1} PASS" -f ($Results.Count - $failed), $Results.Count)
if ($failed -gt 0) { exit 1 }
exit 0