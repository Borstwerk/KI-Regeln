[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('powershell', 'dotnet', 'missing-runtime')]
    [string]$Scenario,
    [Parameter(Mandatory = $true)]
    [string]$Report
)

# Bounded pilot only: NOT a general-purpose command dispatcher.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$reportPath = [System.IO.Path]::GetFullPath($Report)
$reportDir = Split-Path -Parent $reportPath
[void](New-Item -ItemType Directory -Path $reportDir -Force)

$sourceFiles = @{
    'powershell' = @(
        'Evals/Verification-Portable/Run-Pilot.ps1',
        'Evals/Verification-Portable/fixtures/powershell/Discount.ps1',
        'Evals/Verification-Portable/fixtures/powershell/Test-Discount.ps1'
    )
    'dotnet' = @(
        'Evals/Verification-Portable/Run-Pilot.ps1',
        'Evals/Verification-Portable/fixtures/dotnet/Discount.csproj',
        'Evals/Verification-Portable/fixtures/dotnet/Program.cs'
    )
    'missing-runtime' = @('Evals/Verification-Portable/Run-Pilot.ps1')
}

function Get-SourceLines {
    param([string[]]$RelativePaths)
    $result = @()
    # Ordinal case-sensitive sorting: PowerShell's culture sorting differs from
    # Python sorted() for the uppercase Run-Pilot.ps1 versus lowercase fixtures.
    [string[]]$paths = @($RelativePaths)
    [Array]::Sort($paths, [StringComparer]::Ordinal)
    foreach ($rel in $paths) {
        $absolute = Join-Path $root $rel
        if (-not (Test-Path -LiteralPath $absolute -PathType Leaf)) {
            throw "Cannot bind the fixture source: $rel"
        }
        $digest = (Get-FileHash -LiteralPath $absolute -Algorithm SHA256).Hash.ToLowerInvariant()
        $result += ('{0}:{1}' -f $rel.Replace('\', '/'), $digest)
    }
    return $result
}
$manifestLines = @(Get-SourceLines -RelativePaths $sourceFiles[$Scenario])
# The manifest is UTF-8 with LF separators, regardless of the host OS.
$manifestText = ($manifestLines -join [string][char]10) + [string][char]10
$sha = [System.Security.Cryptography.SHA256]::Create()
try {
    $sourceBytes = [System.Text.Encoding]::UTF8.GetBytes($manifestText)
    $sourceDigest = [BitConverter]::ToString($sha.ComputeHash($sourceBytes)).Replace('-', '').ToLowerInvariant()
} finally {
    $sha.Dispose()
}

$tool = switch ($Scenario) {
    'powershell' { 'pwsh' }
    'dotnet' { 'dotnet' }
    'missing-runtime' { 'ki-regeln-intentionally-absent-sdk-0001' }
}
$marker = switch ($Scenario) {
    'powershell' { 'NATIVE_POWERSHELL_ASSERTIONS_PASS' }
    'dotnet' { 'NATIVE_DOTNET_ASSERTIONS_PASS' }
    'missing-runtime' { '' }
}
$command = switch ($Scenario) {
    'powershell' { 'pwsh -NoProfile -NonInteractive -File Test-Discount.ps1' }
    'dotnet' { 'dotnet run --project Discount.csproj --configuration Release --no-launch-profile' }
    'missing-runtime' { 'ki-regeln-intentionally-absent-sdk-0001 --check' }
}

$status = 'NOT_RUN'
$exitValue = $null
$reason = 'Required native runtime was not found on PATH.'
$observedAt = $null
$references = @()
$logName = "$Scenario.native.log"
$logFile = Join-Path $reportDir $logName

$executable = Get-Command -Name $tool -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if ($null -ne $executable) {
    if ($Scenario -eq 'missing-runtime') {
        $status = 'BLOCKED'
        $reason = 'The intentionally absent tool unexpectedly exists; invalid negative control.'
    } else {
        try {
            $argv = if ($Scenario -eq 'powershell') {
                @('-NoProfile', '-NonInteractive', '-File',
                    (Join-Path $root 'Evals/Verification-Portable/fixtures/powershell/Test-Discount.ps1'))
            } else {
                @('run', '--project',
                    (Join-Path $root 'Evals/Verification-Portable/fixtures/dotnet/Discount.csproj'),
                    '--configuration', 'Release', '--no-launch-profile', '--verbosity', 'quiet')
            }
            $output = (& $executable.Source @argv 2>&1 | Out-String -Width 240)
            $exitValue = $LASTEXITCODE
            $observedAt = [DateTime]::UtcNow.ToString('o')
            [System.IO.File]::WriteAllText($logFile, $output, [System.Text.UTF8Encoding]::new($false))
            $references = @($logName)
            if ($null -eq $exitValue) {
                $status = 'UNVERIFIED'
                $reason = 'Native runner returned no observable exit code.'
            } elseif ($exitValue -ne 0) {
                $status = 'FAIL'
                $reason = 'Native process returned a nonzero exit code.'
            } elseif (-not $output.Contains($marker)) {
                $status = 'UNVERIFIED'
                $reason = 'Exit code zero but native completion marker is absent.'
            } else {
                $status = 'PASS'
                $reason = ''
            }
        } catch {
            # Do not leak raw exceptions, paths, or credentials into the report.
            $status = 'UNVERIFIED'
            $reason = 'Native execution or observation failed; result incomplete.'
        }
    }
}

try {
    $afterLines = @(Get-SourceLines -RelativePaths $sourceFiles[$Scenario])
    if (($afterLines -join [string][char]10) -ne ($manifestLines -join [string][char]10)) {
        $status = 'UNVERIFIED'
        $reason = 'Fixture files changed during execution.'
    }
} catch {
    $status = 'UNVERIFIED'
    $reason = 'Fixture source disappeared during execution.'
}

$check = [ordered]@{
    id = "native-$Scenario"
    type = 'unit'
    required_for_claim = $true
    selection = 'project-prescribed'
    tool = $tool
    command_display = $command
    status = $status
    exit_code = $exitValue
    skipped = 0
    evidence_refs = @($references)
}
if ($null -ne $observedAt) { $check.observed_at = $observedAt }
if ($status -ne 'PASS') { $check.reason = $reason }
if ($status -in @('BLOCKED', 'NOT_RUN')) {
    $check.exit_code = $null
    $check.evidence_refs = @()
}

$location = if ($env:GITHUB_ACTIONS -eq 'true') { 'ci' } else { 'local' }
$data = [ordered]@{
    schema_version = 1
    project = [ordered]@{ name = "verification-portable-$Scenario" }
    task = "Run a bounded $Scenario native verification fixture"
    source_state = [ordered]@{
        kind = 'snapshot'
        content_sha256 = $sourceDigest
        digest_scope = 'Pilot source manifest: sorted relative/path:sha256(file) UTF-8 lines with LF and terminal LF'
    }
    environment = [ordered]@{
        location = $location
        os = [System.Runtime.InteropServices.RuntimeInformation]::OSDescription
        runtime = "PowerShell $($PSVersionTable.PSVersion); native target $tool"
    }
    checks = @($check)
}
$json = $data | ConvertTo-Json -Depth 9
[System.IO.File]::WriteAllText($reportPath, ($json + [string][char]10), [System.Text.UTF8Encoding]::new($false))
Write-Host ("{0}: {1} -> {2}" -f $Scenario, $status, $reportPath)

if ($Scenario -eq 'missing-runtime') {
    if ($status -eq 'NOT_RUN') { exit 0 } # Runner success means the negative control was observed.
    exit 1
}
if ($status -eq 'PASS') { exit 0 }
if ($status -eq 'NOT_RUN') { exit 2 }
exit 1
