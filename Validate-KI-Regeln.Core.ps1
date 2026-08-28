[CmdletBinding()]
param(
    [switch]$Quick,
    [switch]$Full,
    [switch]$Release,
    [switch]$WarningsAsErrors,
    [switch]$NoBootstrap
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

$RepoRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$Mode = 'Full'
$selectedModes = @(@($Quick, $Full, $Release) | Where-Object { $_ })
if ($selectedModes.Count -gt 1) {
    Write-Error 'Use only one of -Quick, -Full, or -Release.'
    exit 2
}
if ($Quick) { $Mode = 'Quick' }
elseif ($Release) { $Mode = 'Release' }

$StateRoot = if ($env:KI_REGELN_VALIDATION_STATE_DIR) {
    [System.IO.Path]::GetFullPath($env:KI_REGELN_VALIDATION_STATE_DIR)
} else {
    Join-Path $RepoRoot '.validation'
}
$RuntimeRoot = Join-Path $StateRoot 'runtime'
$LogsRoot = Join-Path $StateRoot 'logs'
$LatestJson = Join-Path $StateRoot 'latest.json'
$LatestMarkdown = Join-Path $StateRoot 'latest.md'
$ManifestPath = Join-Path $RepoRoot 'tools/local_validation/runtime-manifest.json'
$RequirementsPath = Join-Path $RepoRoot 'tools/local_validation/requirements.lock'
$RunId = (Get-Date).ToUniversalTime().ToString('yyyyMMdd-HHmmss')
$RunLog = Join-Path $LogsRoot ("validation-{0}.log" -f $RunId)

$script:Checks = New-Object System.Collections.ArrayList
$script:Findings = New-Object System.Collections.ArrayList
$script:Counts = [ordered]@{}
$script:RuntimeInfo = [ordered]@{
    bootstrap_performed = $false
    uv_version = $null
    python_version = $null
}
$script:InfrastructureFailure = $false

function New-Utf8NoBom {
    return New-Object System.Text.UTF8Encoding($false)
}

function Write-TextFile {
    param([string]$Path, [string]$Text)
    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Text, (New-Utf8NoBom))
}

function Append-Log {
    param([string]$Text)
    $line = "[{0}] {1}{2}" -f (Get-Date).ToUniversalTime().ToString('o'), $Text, [Environment]::NewLine
    [System.IO.File]::AppendAllText($RunLog, $line, (New-Utf8NoBom))
}

function Add-Check {
    param(
        [string]$Name,
        [ValidateSet('PASS','WARN','FAIL','INFO','NOT RUN','SKIP')]
        [string]$Status,
        [string]$Code = '',
        [string]$Message = '',
        [long]$DurationMs = 0
    )
    [void]$script:Checks.Add([ordered]@{
        name = $Name
        status = $Status
        code = $Code
        message = $Message
        duration_ms = $DurationMs
    })
}

function Add-Finding {
    param(
        [ValidateSet('warning','error','info')]
        [string]$Severity,
        [string]$Code,
        [string]$Message,
        [string]$Path = ''
    )
    [void]$script:Findings.Add([ordered]@{
        severity = $Severity
        code = $Code
        message = $Message
        path = $Path
    })
}

function Invoke-Captured {
    param(
        [string]$FilePath,
        [string[]]$Arguments,
        [string]$WorkingDirectory = $RepoRoot
    )
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FilePath
    $psi.WorkingDirectory = $WorkingDirectory
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    $quotedArguments = @()
    foreach ($arg in $Arguments) {
        if ($arg -match '[\s"]') {
            $quotedArguments += ('"' + ($arg -replace '"', '\"') + '"')
        } else {
            $quotedArguments += $arg
        }
    }
    $psi.Arguments = ($quotedArguments -join ' ')

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $psi
    $watch = [System.Diagnostics.Stopwatch]::StartNew()
    [void]$process.Start()
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    $watch.Stop()

    Append-Log ("COMMAND: {0} {1}`nEXIT: {2}`nSTDOUT:`n{3}`nSTDERR:`n{4}" -f
        $FilePath, ($Arguments -join ' '), $process.ExitCode, $stdout, $stderr)

    return [pscustomobject]@{
        ExitCode = $process.ExitCode
        StdOut = $stdout
        StdErr = $stderr
        DurationMs = $watch.ElapsedMilliseconds
    }
}

function Invoke-Git {
    param([string[]]$Arguments)
    return Invoke-Captured -FilePath 'git.exe' -Arguments $Arguments
}

function Test-GitAvailable {
    try {
        $result = Invoke-Captured -FilePath 'git.exe' -Arguments @('--version')
        return ($result.ExitCode -eq 0)
    } catch {
        Append-Log ("Git unavailable: {0}" -f $_.Exception.Message)
        return $false
    }
}

function Get-RepoHead {
    if (-not (Test-GitAvailable)) { return $null }
    $head = Invoke-Git @('rev-parse', 'HEAD')
    if ($head.ExitCode -eq 0) { return $head.StdOut.Trim() }
    return $null
}

function Get-PlatformAsset {
    param($Manifest)
    if ($env:OS -ne 'Windows_NT') {
        throw 'UNSUPPORTED_PLATFORM: Local bootstrap currently supports Windows only.'
    }
    $arch = $env:PROCESSOR_ARCHITECTURE
    if ($arch -eq 'AMD64') { return $Manifest.uv.assets.'windows-x64' }
    if ($arch -eq 'ARM64') { return $Manifest.uv.assets.'windows-arm64' }
    throw ("UNSUPPORTED_ARCHITECTURE: {0}" -f $arch)
}

function Test-RuntimeState {
    param($Manifest, [string]$PythonExe, [string]$StampPath)
    if (-not (Test-Path -LiteralPath $PythonExe) -or -not (Test-Path -LiteralPath $StampPath)) {
        return $false
    }
    try {
        $stamp = Get-Content -Raw -LiteralPath $StampPath | ConvertFrom-Json
        $manifestHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $ManifestPath).Hash.ToLowerInvariant()
        $requirementsHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $RequirementsPath).Hash.ToLowerInvariant()
        if ($stamp.manifest_sha256 -ne $manifestHash -or $stamp.requirements_sha256 -ne $requirementsHash) {
            return $false
        }
        $probe = Invoke-Captured -FilePath $PythonExe -Arguments @('-c', 'import platform; print(platform.python_version())')
        if ($probe.ExitCode -ne 0 -or $probe.StdOut.Trim() -ne [string]$Manifest.python.version) {
            return $false
        }
        $script:RuntimeInfo.python_version = $probe.StdOut.Trim()
        $script:RuntimeInfo.uv_version = [string]$stamp.uv_version
        return $true
    } catch {
        Append-Log ("Runtime state probe failed: {0}" -f $_.Exception.Message)
        return $false
    }
}

function Ensure-PortableRuntime {
    $watch = [System.Diagnostics.Stopwatch]::StartNew()
    if (-not (Test-Path -LiteralPath $ManifestPath)) {
        throw 'RUNTIME_MANIFEST_MISSING: tools/local_validation/runtime-manifest.json'
    }
    if (-not (Test-Path -LiteralPath $RequirementsPath)) {
        throw 'RUNTIME_LOCK_MISSING: tools/local_validation/requirements.lock'
    }

    $manifest = Get-Content -Raw -LiteralPath $ManifestPath | ConvertFrom-Json
    $venvDir = Join-Path $RuntimeRoot 'venv'
    $pythonExe = Join-Path $venvDir 'Scripts/python.exe'
    $stampPath = Join-Path $RuntimeRoot 'state.json'

    if (Test-RuntimeState -Manifest $manifest -PythonExe $pythonExe -StampPath $stampPath) {
        $watch.Stop()
        Add-Check -Name 'Portable runtime' -Status 'PASS' -Message ("CPython {0}, cached locally" -f $script:RuntimeInfo.python_version) -DurationMs $watch.ElapsedMilliseconds
        return $pythonExe
    }

    if ($NoBootstrap) {
        throw 'RUNTIME_MISSING: portable runtime is absent or stale and -NoBootstrap was requested.'
    }

    $asset = Get-PlatformAsset -Manifest $manifest
    New-Item -ItemType Directory -Force -Path $RuntimeRoot | Out-Null
    $downloadDir = Join-Path $RuntimeRoot 'downloads'
    $uvDir = Join-Path $RuntimeRoot 'uv'
    $pythonInstallDir = Join-Path $RuntimeRoot 'python'
    $pythonBinDir = Join-Path $RuntimeRoot 'python-bin'
    $cacheDir = Join-Path $RuntimeRoot 'cache'
    foreach ($dir in @($downloadDir, $uvDir, $pythonInstallDir, $pythonBinDir, $cacheDir)) {
        New-Item -ItemType Directory -Force -Path $dir | Out-Null
    }

    $zipPath = Join-Path $downloadDir $asset.file
    $downloadRequired = $true
    if (Test-Path -LiteralPath $zipPath) {
        $existingHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipPath).Hash.ToLowerInvariant()
        if ($existingHash -eq ([string]$asset.sha256).ToLowerInvariant()) {
            $downloadRequired = $false
        } else {
            Remove-Item -Force -LiteralPath $zipPath
        }
    }

    if ($downloadRequired) {
        Write-Host ("Bootstrap: lade uv {0} kontrolliert herunter ..." -f $manifest.uv.version)
        Append-Log ("BOOTSTRAP DOWNLOAD: {0}" -f $asset.url)
        if (([Net.ServicePointManager]::SecurityProtocol -band [Net.SecurityProtocolType]::Tls12) -eq 0) {
            [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
        }
        Invoke-WebRequest -Uri ([string]$asset.url) -OutFile $zipPath -UseBasicParsing
    }

    $actualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipPath).Hash.ToLowerInvariant()
    if ($actualHash -ne ([string]$asset.sha256).ToLowerInvariant()) {
        throw ("UV_HASH_MISMATCH: expected {0}, got {1}" -f $asset.sha256, $actualHash)
    }

    if (Test-Path -LiteralPath $uvDir) {
        Get-ChildItem -LiteralPath $uvDir -Force | Remove-Item -Recurse -Force
    }
    Expand-Archive -LiteralPath $zipPath -DestinationPath $uvDir -Force
    $uvExe = Get-ChildItem -Path $uvDir -Recurse -Filter 'uv.exe' | Select-Object -First 1
    if (-not $uvExe) {
        throw 'UV_BOOTSTRAP_FAILED: uv.exe not found after verified archive extraction.'
    }

    $uvProbe = Invoke-Captured -FilePath $uvExe.FullName -Arguments @('--version')
    if ($uvProbe.ExitCode -ne 0 -or $uvProbe.StdOut -notmatch [regex]::Escape([string]$manifest.uv.version)) {
        throw ("UV_VERSION_MISMATCH: expected {0}, got {1}" -f $manifest.uv.version, $uvProbe.StdOut.Trim())
    }
    $script:RuntimeInfo.uv_version = [string]$manifest.uv.version

    $savedEnv = @{}
    foreach ($name in @('UV_CACHE_DIR','UV_PYTHON_INSTALL_DIR','UV_PYTHON_BIN_DIR','UV_MANAGED_PYTHON','UV_NO_CONFIG','UV_NO_SYSTEM_CONFIG')) {
        $savedEnv[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
    }
    try {
        $env:UV_CACHE_DIR = $cacheDir
        $env:UV_PYTHON_INSTALL_DIR = $pythonInstallDir
        $env:UV_PYTHON_BIN_DIR = $pythonBinDir
        $env:UV_MANAGED_PYTHON = 'true'
        $env:UV_NO_CONFIG = '1'
        $env:UV_NO_SYSTEM_CONFIG = '1'

        $install = Invoke-Captured -FilePath $uvExe.FullName -Arguments @(
            'python', 'install', [string]$manifest.python.version,
            '--managed-python', '--no-progress', '--no-registry', '--no-bin'
        )
        if ($install.ExitCode -ne 0) {
            throw ("PYTHON_BOOTSTRAP_FAILED: {0}" -f (($install.StdErr -split "`r?`n")[0]))
        }

        if (Test-Path -LiteralPath $venvDir) {
            Remove-Item -Recurse -Force -LiteralPath $venvDir
        }
        $createVenv = Invoke-Captured -FilePath $uvExe.FullName -Arguments @(
            'venv', $venvDir, '--python', [string]$manifest.python.version,
            '--managed-python', '--no-progress'
        )
        if ($createVenv.ExitCode -ne 0) {
            throw ("VENV_BOOTSTRAP_FAILED: {0}" -f (($createVenv.StdErr -split "`r?`n")[0]))
        }
        if (-not (Test-Path -LiteralPath $pythonExe)) {
            throw 'VENV_BOOTSTRAP_FAILED: local python.exe was not created.'
        }

        $sync = Invoke-Captured -FilePath $uvExe.FullName -Arguments @(
            'pip', 'sync', '--python', $pythonExe, $RequirementsPath, '--no-progress'
        )
        if ($sync.ExitCode -ne 0) {
            throw ("DEPENDENCY_BOOTSTRAP_FAILED: {0}" -f (($sync.StdErr -split "`r?`n")[0]))
        }
    } finally {
        foreach ($name in $savedEnv.Keys) {
            [Environment]::SetEnvironmentVariable($name, $savedEnv[$name], 'Process')
        }
    }

    $probe = Invoke-Captured -FilePath $pythonExe -Arguments @(
        '-c', 'import platform, yaml, jsonschema; print(platform.python_version()); print(yaml.__version__); print(jsonschema.__version__)'
    )
    if ($probe.ExitCode -ne 0) {
        throw 'RUNTIME_VERIFY_FAILED: Python dependencies cannot be imported.'
    }
    $probeLines = @($probe.StdOut -split "`r?`n" | Where-Object { $_ })
    if ($probeLines.Count -lt 1 -or $probeLines[0].Trim() -ne [string]$manifest.python.version) {
        throw ("PYTHON_VERSION_MISMATCH: expected {0}" -f $manifest.python.version)
    }

    $script:RuntimeInfo.bootstrap_performed = $true
    $script:RuntimeInfo.python_version = $probeLines[0].Trim()
    $stamp = [ordered]@{
        schema_version = 1
        created_at = (Get-Date).ToUniversalTime().ToString('o')
        uv_version = [string]$manifest.uv.version
        python_version = [string]$manifest.python.version
        manifest_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $ManifestPath).Hash.ToLowerInvariant()
        requirements_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $RequirementsPath).Hash.ToLowerInvariant()
    }
    Write-TextFile -Path $stampPath -Text (($stamp | ConvertTo-Json -Depth 8) + "`n")

    $watch.Stop()
    Add-Check -Name 'Portable runtime' -Status 'PASS' -Message ("CPython {0}, uv {1}; first bootstrap completed" -f $manifest.python.version, $manifest.uv.version) -DurationMs $watch.ElapsedMilliseconds
    return $pythonExe
}

function Parse-ValidatorOutput {
    param([string]$Output)
    foreach ($line in ($Output -split "`r?`n")) {
        if ($line -match '^ERROR\s+([A-Z0-9_-]+):\s*(.*)$') {
            Add-Finding -Severity 'error' -Code $matches[1] -Message $matches[2]
        } elseif ($line -match '^WARNING\s+([A-Z0-9_-]+):\s*(.*)$') {
            Add-Finding -Severity 'warning' -Code $matches[1] -Message $matches[2]
        } elseif ($line -match '^Validated skills:\s*(\d+)') {
            $script:Counts.skills = [int]$matches[1]
        } elseif ($line -match '^Validated eval files:\s*(\d+)') {
            $script:Counts.evalpacks = [int]$matches[1]
        } elseif ($line -match '^Validated workflows:\s*(\d+)') {
            $script:Counts.workflows = [int]$matches[1]
        } elseif ($line -match '^Validated golden tasks:\s*(\d+)') {
            $script:Counts.golden_tasks = [int]$matches[1]
        }
    }
}

function Run-StructuralValidation {
    param([string]$PythonExe)
    $args = @((Join-Path $RepoRoot 'tools/repo_validator.py'))
    if ($WarningsAsErrors) { $args += '--warnings-as-errors' }
    $result = Invoke-Captured -FilePath $PythonExe -Arguments $args
    Parse-ValidatorOutput -Output $result.StdOut

    $errors = @($script:Findings | Where-Object { $_.severity -eq 'error' }).Count
    $warnings = @($script:Findings | Where-Object { $_.severity -eq 'warning' }).Count
    if ($result.ExitCode -eq 0) {
        Add-Check -Name 'Structural validation' -Status $(if ($warnings) { 'WARN' } else { 'PASS' }) -Message ("canonical repo_validator.py; errors={0}, warnings={1}" -f $errors, $warnings) -DurationMs $result.DurationMs
    } else {
        if ($errors -eq 0 -and -not ($WarningsAsErrors -and $warnings -gt 0)) {
            Add-Finding -Severity 'error' -Code 'VALIDATOR_PROCESS' -Message 'repo_validator.py exited non-zero; see log for technical details.'
        }
        Add-Check -Name 'Structural validation' -Status 'FAIL' -Code 'REPO_VALIDATOR' -Message ("canonical repo_validator.py exited {0}" -f $result.ExitCode) -DurationMs $result.DurationMs
    }
}

function Run-EvalCoverageAudit {
    param([string]$PythonExe)
    $result = Invoke-Captured -FilePath $PythonExe -Arguments @(
        (Join-Path $RepoRoot 'tools/eval_coverage_audit.py')
    )
    if ($result.ExitCode -ne 0) {
        Add-Finding -Severity 'error' -Code 'EVAL_COVERAGE_PROCESS' -Message 'eval_coverage_audit.py failed; see log.'
        Add-Check -Name 'Eval coverage audit' -Status 'FAIL' -Code 'EVAL_COVERAGE_PROCESS' -DurationMs $result.DurationMs
        return
    }

    $data = $null
    try {
        $data = $result.StdOut | ConvertFrom-Json
    } catch {
        Add-Finding -Severity 'error' -Code 'EVAL_COVERAGE_JSON' -Message ("Coverage audit returned invalid JSON: {0}" -f $_.Exception.Message)
        Add-Check -Name 'Eval coverage audit' -Status 'FAIL' -Code 'EVAL_COVERAGE_JSON' -DurationMs $result.DurationMs
        return
    }

    $requiredFields = @(
        'skill_count',
        'eval_file_count',
        'case_count',
        'coverage_counts',
        'skills_without_evals',
        'one_sided_signal_count',
        'skills',
        'notes'
    )
    $availableFields = @($data.PSObject.Properties.Name)
    $missingFields = @($requiredFields | Where-Object { $_ -notin $availableFields })
    if ($missingFields.Count -gt 0) {
        Add-Finding -Severity 'error' -Code 'EVAL_COVERAGE_SCHEMA' -Message ("Coverage audit output is missing expected root field(s): {0}" -f ($missingFields -join ', '))
        Add-Check -Name 'Eval coverage audit' -Status 'FAIL' -Code 'EVAL_COVERAGE_SCHEMA' -DurationMs $result.DurationMs
        return
    }

    try {
        $script:Counts.skills = [int]$data.skill_count
        $script:Counts.evalpacks = [int]$data.eval_file_count
        $script:Counts.defined_cases = [int]$data.case_count
        if ($null -eq $data.coverage_counts) {
            throw 'coverage_counts is null.'
        }
        foreach ($property in $data.coverage_counts.PSObject.Properties) {
            $script:Counts[("coverage_{0}" -f $property.Name)] = [int]$property.Value
        }
        $script:Counts.skills_without_evals = @($data.skills_without_evals).Count
        $script:Counts.heuristic_audit_signals = [int]$data.one_sided_signal_count
    } catch {
        Add-Finding -Severity 'error' -Code 'EVAL_COVERAGE_PROCESSING' -Message ("Coverage audit JSON parsed, but field processing failed: {0}" -f $_.Exception.Message)
        Add-Check -Name 'Eval coverage audit' -Status 'FAIL' -Code 'EVAL_COVERAGE_PROCESSING' -DurationMs $result.DurationMs
        return
    }

    Add-Check -Name 'Eval coverage audit' -Status 'PASS' -Message 'inventory/report only; defined cases are not behavioral results' -DurationMs $result.DurationMs
}

function Run-CurrentTreeExposure {
    param([string]$PythonExe)
    $output = Join-Path $StateRoot 'current-tree.json'
    $result = Invoke-Captured -FilePath $PythonExe -Arguments @(
        (Join-Path $RepoRoot 'tools/open_source_readiness_audit.py'),
        '--output', $output
    )
    if ($result.ExitCode -ne 0 -or -not (Test-Path -LiteralPath $output)) {
        Add-Finding -Severity 'error' -Code 'CURRENT_TREE_SCAN' -Message 'Current-tree exposure scanner failed; see log.'
        Add-Check -Name 'Current-tree exposure' -Status 'FAIL' -Code 'CURRENT_TREE_SCAN' -DurationMs $result.DurationMs
        return
    }

    $data = Get-Content -Raw -LiteralPath $output | ConvertFrom-Json
    $secretFindings = @($data.current_tree.findings | Where-Object { $_.severity -eq 'potential-secret' })
    $contextFindings = @($data.current_tree.findings | Where-Object { $_.severity -eq 'review-context' })
    $script:Counts.current_tree_potential_secret = $secretFindings.Count
    $script:Counts.current_tree_review_context = $contextFindings.Count
    $script:Counts.current_tree_binary_files = @($data.current_tree.binaries).Count

    foreach ($finding in $secretFindings) {
        Add-Finding -Severity 'error' -Code ("EXPOSURE_{0}" -f ([string]$finding.class).ToUpperInvariant().Replace('-', '_')) -Message ("potential secret metadata at line {0}" -f $finding.line) -Path ([string]$finding.path)
    }
    foreach ($finding in $contextFindings) {
        Add-Finding -Severity 'warning' -Code ("CONTEXT_{0}" -f ([string]$finding.class).ToUpperInvariant().Replace('-', '_')) -Message ("review-context metadata at line {0}" -f $finding.line) -Path ([string]$finding.path)
    }

    if ($secretFindings.Count -gt 0) {
        Add-Check -Name 'Current-tree exposure' -Status 'FAIL' -Code 'POTENTIAL_SECRET' -Message ("potential-secret findings={0}" -f $secretFindings.Count) -DurationMs $result.DurationMs
    } elseif ($contextFindings.Count -gt 0) {
        Add-Check -Name 'Current-tree exposure' -Status 'WARN' -Message ("review-context findings={0}; existing CI treats these as review signals" -f $contextFindings.Count) -DurationMs $result.DurationMs
    } else {
        Add-Check -Name 'Current-tree exposure' -Status 'PASS' -DurationMs $result.DurationMs
    }

    if ($data.quellen_registry_crosscheck) {
        $script:Counts.unregistered_source_urls = [int]$data.quellen_registry_crosscheck.unregistered_url_count
    }
}

function Run-HistoryExposure {
    param([string]$PythonExe)
    $shallow = Invoke-Git @('rev-parse', '--is-shallow-repository')
    if ($shallow.ExitCode -ne 0) {
        $script:InfrastructureFailure = $true
        Add-Finding -Severity 'error' -Code 'HISTORY_GIT' -Message 'Cannot determine whether the repository has full history.'
        Add-Check -Name 'Reachable-history exposure' -Status 'FAIL' -Code 'HISTORY_GIT'
        return
    }
    if ($shallow.StdOut.Trim().ToLowerInvariant() -eq 'true') {
        $script:InfrastructureFailure = $true
        Add-Finding -Severity 'error' -Code 'HISTORY_SHALLOW' -Message 'Release validation requires a full-history checkout; shallow history would give a misleading result.'
        Add-Check -Name 'Reachable-history exposure' -Status 'FAIL' -Code 'HISTORY_SHALLOW'
        return
    }

    $output = Join-Path $StateRoot 'reachable-history.json'
    $result = Invoke-Captured -FilePath $PythonExe -Arguments @(
        (Join-Path $RepoRoot 'tools/history_exposure_scan.py'), $output
    )
    if ($result.ExitCode -ne 0 -or -not (Test-Path -LiteralPath $output)) {
        $script:InfrastructureFailure = $true
        Add-Finding -Severity 'error' -Code 'HISTORY_SCAN' -Message 'Reachable-history exposure scanner failed; see log.'
        Add-Check -Name 'Reachable-history exposure' -Status 'FAIL' -Code 'HISTORY_SCAN' -DurationMs $result.DurationMs
        return
    }

    $data = Get-Content -Raw -LiteralPath $output | ConvertFrom-Json
    $secretFindings = @($data.findings | Where-Object { $_.severity -eq 'potential-secret' })
    $contextFindings = @($data.findings | Where-Object { $_.severity -eq 'review-context' })
    $script:Counts.reachable_commits = [int]$data.commit_count
    $script:Counts.reachable_unique_blobs = [int]$data.unique_reachable_blob_count
    $script:Counts.history_potential_secret = $secretFindings.Count
    $script:Counts.history_review_context = $contextFindings.Count

    foreach ($finding in $secretFindings) {
        Add-Finding -Severity 'error' -Code ("HISTORY_EXPOSURE_{0}" -f ([string]$finding.class).ToUpperInvariant().Replace('-', '_')) -Message ("potential secret metadata at line {0}, commit {1}" -f $finding.line, ([string]$finding.commit).Substring(0,12)) -Path ([string]$finding.path)
    }
    foreach ($finding in $contextFindings) {
        Add-Finding -Severity 'warning' -Code ("HISTORY_CONTEXT_{0}" -f ([string]$finding.class).ToUpperInvariant().Replace('-', '_')) -Message ("review-context metadata at line {0}, commit {1}" -f $finding.line, ([string]$finding.commit).Substring(0,12)) -Path ([string]$finding.path)
    }

    if ($secretFindings.Count -gt 0) {
        Add-Check -Name 'Reachable-history exposure' -Status 'FAIL' -Code 'POTENTIAL_SECRET' -Message ("potential-secret findings={0}" -f $secretFindings.Count) -DurationMs $result.DurationMs
    } elseif ($contextFindings.Count -gt 0) {
        Add-Check -Name 'Reachable-history exposure' -Status 'WARN' -Message ("review-context findings={0}; existing CI treats these as review signals" -f $contextFindings.Count) -DurationMs $result.DurationMs
    } else {
        Add-Check -Name 'Reachable-history exposure' -Status 'PASS' -DurationMs $result.DurationMs
    }
}

function Write-ConsoleReport {
    param([string]$Overall, [int]$ExitCode)
    Write-Host ''
    Write-Host 'KI-Regeln Local Validation'
    Write-Host '==========================='
    Write-Host ("Mode                          {0}" -f $Mode)
    Write-Host ''

    foreach ($check in $script:Checks) {
        Write-Host ("{0,-30}{1}" -f $check.name, $check.status)
    }
    Write-Host ("{0,-30}{1}" -f 'Behavioral validation', 'NOT RUN')

    if ($script:Counts.Count -gt 0) {
        Write-Host ''
        if ($script:Counts.Contains('skills')) { Write-Host ("{0,-30}{1}" -f 'Skills', $script:Counts.skills) }
        if ($script:Counts.Contains('evalpacks')) { Write-Host ("{0,-30}{1}" -f 'Evalpacks', $script:Counts.evalpacks) }
        if ($script:Counts.Contains('defined_cases')) { Write-Host ("{0,-30}{1}" -f 'Defined cases', $script:Counts.defined_cases) }
        foreach ($name in @('coverage_partial','coverage_none','coverage_core','coverage_broad')) {
            if ($script:Counts.Contains($name)) {
                Write-Host ("{0,-30}{1}" -f ($name.Replace('_',' ')), $script:Counts[$name])
            }
        }
    }

    $visible = @($script:Findings | Where-Object { $_.severity -ne 'info' })
    if ($visible.Count -gt 0) {
        Write-Host ''
        foreach ($finding in $visible) {
            Write-Host ("{0}  {1}" -f $finding.code, $finding.severity.ToUpperInvariant())
            Write-Host $finding.message
            if ($finding.path) { Write-Host ("Path: {0}" -f $finding.path) }
            Write-Host ''
        }
    }

    Write-Host ("{0,-30}{1}" -f 'OVERALL', $Overall)
    Write-Host ("{0,-30}{1}" -f 'Exit code', $ExitCode)
    Write-Host ("{0,-30}{1}" -f 'JSON report', $LatestJson)
    Write-Host ("{0,-30}{1}" -f 'Markdown report', $LatestMarkdown)
    Write-Host ("{0,-30}{1}" -f 'Technical log', $RunLog)
}

function Write-Reports {
    param(
        [string]$Overall,
        [int]$ExitCode,
        [string]$Head
    )
    $report = [ordered]@{
        schema_version = 1
        generated_at = (Get-Date).ToUniversalTime().ToString('o')
        mode = $Mode
        repository_root = $RepoRoot
        repository_head = $Head
        overall = $Overall
        exit_code = $ExitCode
        warnings_as_errors = [bool]$WarningsAsErrors
        behavioral_validation = 'NOT RUN'
        runtime = $script:RuntimeInfo
        counts = $script:Counts
        checks = $script:Checks
        findings = $script:Findings
        artifacts = [ordered]@{
            json = $LatestJson
            markdown = $LatestMarkdown
            log = $RunLog
        }
    }
    Write-TextFile -Path $LatestJson -Text (($report | ConvertTo-Json -Depth 12) + "`n")

    $md = New-Object System.Text.StringBuilder
    [void]$md.AppendLine('# KI-Regeln Local Validation')
    [void]$md.AppendLine('')
    [void]$md.AppendLine(('- Mode: `{0}`' -f $Mode))
    [void]$md.AppendLine(('- Repository Head: `{0}`' -f $Head))
    [void]$md.AppendLine(("- Overall: **{0}**" -f $Overall))
    [void]$md.AppendLine(('- Exit code: `{0}`' -f $ExitCode))
    [void]$md.AppendLine('- Behavioral validation: **NOT RUN**')
    [void]$md.AppendLine('')
    [void]$md.AppendLine('## Checks')
    [void]$md.AppendLine('')
    [void]$md.AppendLine('| Check | Status | Code | Message |')
    [void]$md.AppendLine('| --- | --- | --- | --- |')
    foreach ($check in $script:Checks) {
        $message = ([string]$check.message).Replace('|','\|').Replace("`r",' ').Replace("`n",' ')
        [void]$md.AppendLine(('| {0} | {1} | {2} | {3} |' -f $check.name, $check.status, $check.code, $message))
    }
    [void]$md.AppendLine('| Behavioral validation | NOT RUN |  | Structural harness does not execute behavioral evals. |')
    [void]$md.AppendLine('')
    [void]$md.AppendLine('## Counts')
    [void]$md.AppendLine('')
    foreach ($key in $script:Counts.Keys) {
        [void]$md.AppendLine(("- {0}: {1}" -f $key, $script:Counts[$key]))
    }
    if ($script:Findings.Count -gt 0) {
        [void]$md.AppendLine('')
        [void]$md.AppendLine('## Findings')
        [void]$md.AppendLine('')
        foreach ($finding in $script:Findings) {
            [void]$md.AppendLine(("### {0} — {1}" -f $finding.code, $finding.severity.ToUpperInvariant()))
            [void]$md.AppendLine('')
            [void]$md.AppendLine([string]$finding.message)
            if ($finding.path) {
                [void]$md.AppendLine('')
                [void]$md.AppendLine(('Path: `{0}`' -f $finding.path))
            }
            [void]$md.AppendLine('')
        }
    }
    Write-TextFile -Path $LatestMarkdown -Text $md.ToString()
}

New-Item -ItemType Directory -Force -Path $StateRoot, $LogsRoot | Out-Null
Write-TextFile -Path $RunLog -Text ("KI-Regeln Local Validation log`nMode: {0}`nStarted: {1}`n`n" -f $Mode, (Get-Date).ToUniversalTime().ToString('o'))

$head = $null
try {
    $required = @(
        'skill-catalog.yml',
        'workflow-index.yml',
        'tools/repo_validator.py',
        'tools/eval_coverage_audit.py',
        'tools/open_source_readiness_audit.py',
        'tools/history_exposure_scan.py'
    )
    $missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $RepoRoot $_)) })
    if ($missing.Count -gt 0) {
        $script:InfrastructureFailure = $true
        foreach ($item in $missing) {
            Add-Finding -Severity 'error' -Code 'REPOSITORY_FILE_MISSING' -Message 'Required harness input is missing.' -Path $item
        }
        Add-Check -Name 'Repository' -Status 'FAIL' -Code 'REPOSITORY_FILE_MISSING'
    } else {
        Add-Check -Name 'Repository' -Status 'PASS'
    }

    $gitAvailable = Test-GitAvailable
    if ($gitAvailable) {
        $rootProbe = Invoke-Git @('rev-parse', '--show-toplevel')
        if ($rootProbe.ExitCode -eq 0) {
            $actualRoot = [System.IO.Path]::GetFullPath($rootProbe.StdOut.Trim())
            if ($actualRoot.TrimEnd('\') -ne $RepoRoot.TrimEnd('\')) {
                $script:InfrastructureFailure = $true
                Add-Finding -Severity 'error' -Code 'REPOSITORY_ROOT' -Message ("Git root is {0}, harness root is {1}" -f $actualRoot, $RepoRoot)
                Add-Check -Name 'Git repository' -Status 'FAIL' -Code 'REPOSITORY_ROOT'
            } else {
                Add-Check -Name 'Git repository' -Status 'PASS'
            }
        }
        $head = Get-RepoHead
        $status = Invoke-Git @('status', '--porcelain')
        if ($status.ExitCode -eq 0 -and $status.StdOut.Trim()) {
            Add-Finding -Severity 'warning' -Code 'WORKTREE_DIRTY' -Message 'Working tree contains local changes; validation includes the current local tree.'
            Add-Check -Name 'Git working tree' -Status 'WARN' -Code 'WORKTREE_DIRTY'
        } elseif ($status.ExitCode -eq 0) {
            Add-Check -Name 'Git working tree' -Status 'PASS'
        }
    } else {
        if ($Mode -eq 'Release') {
            $script:InfrastructureFailure = $true
            Add-Finding -Severity 'error' -Code 'GIT_MISSING' -Message 'Release validation requires Git for current-tree and reachable-history exposure checks.'
            Add-Check -Name 'Git repository' -Status 'FAIL' -Code 'GIT_MISSING'
        } else {
            Add-Finding -Severity 'warning' -Code 'GIT_MISSING' -Message 'Git is unavailable; structural validation can run, but repository state cannot be reported.'
            Add-Check -Name 'Git repository' -Status 'WARN' -Code 'GIT_MISSING'
        }
    }

    if (-not $script:InfrastructureFailure) {
        $pythonExe = Ensure-PortableRuntime
        Run-StructuralValidation -PythonExe $pythonExe

        if ($Mode -in @('Full','Release')) {
            Run-EvalCoverageAudit -PythonExe $pythonExe
        } else {
            Add-Check -Name 'Eval coverage audit' -Status 'SKIP' -Message 'Use -Full or -Release for the coverage inventory report.'
        }

        if ($Mode -eq 'Release') {
            Run-CurrentTreeExposure -PythonExe $pythonExe
            Run-HistoryExposure -PythonExe $pythonExe
        } else {
            Add-Check -Name 'Current-tree exposure' -Status 'SKIP' -Message 'Use -Release.'
            Add-Check -Name 'Reachable-history exposure' -Status 'SKIP' -Message 'Use -Release.'
        }
    }
} catch {
    $script:InfrastructureFailure = $true
    $short = $_.Exception.Message
    $runtimeCode = 'HARNESS_RUNTIME'
    if ($short -match '^([A-Z0-9_-]+):') { $runtimeCode = $matches[1] }
    Add-Finding -Severity 'error' -Code $runtimeCode -Message $short
    Add-Check -Name 'Harness execution' -Status 'FAIL' -Code $runtimeCode
    Append-Log ("UNHANDLED EXCEPTION:`n{0}" -f ($_ | Out-String))
}

$errorCount = @($script:Findings | Where-Object { $_.severity -eq 'error' }).Count
$warningCount = @($script:Findings | Where-Object { $_.severity -eq 'warning' }).Count
$failedChecks = @($script:Checks | Where-Object { $_.status -eq 'FAIL' }).Count

$exitCode = 0
if ($script:InfrastructureFailure) {
    $exitCode = 2
} elseif ($errorCount -gt 0 -or $failedChecks -gt 0) {
    $exitCode = 1
} elseif ($WarningsAsErrors -and $warningCount -gt 0) {
    $exitCode = 1
}

$overall = if ($exitCode -eq 0) { 'PASS' } else { 'FAIL' }
Write-Reports -Overall $overall -ExitCode $exitCode -Head $head
Write-ConsoleReport -Overall $overall -ExitCode $exitCode
exit $exitCode
