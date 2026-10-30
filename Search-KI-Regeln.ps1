[CmdletBinding(DefaultParameterSetName = 'Query')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Query')][string]$Query,
    [Parameter(Mandatory, ParameterSetName = 'Build')][switch]$Build,
    [Parameter(Mandatory, ParameterSetName = 'Status')][switch]$Status,
    [Parameter(Mandatory, ParameterSetName = 'Setup')][switch]$Setup,
    [Parameter(Mandatory, ParameterSetName = 'ListSkills')][switch]$ListSkills,
    [Parameter(ParameterSetName = 'Query')][Parameter(ParameterSetName = 'ListSkills')][string]$Limit,
    [Parameter(ParameterSetName = 'Query')][Parameter(ParameterSetName = 'ListSkills')][string]$Cursor,
    [switch]$Routing,
    [string]$NodePath = 'node',
    [string]$PnpmPath = 'pnpm'
)
$ErrorActionPreference = 'Stop'
$runtime = Join-Path $PSScriptRoot '.validation/qmd-runtime'
function Resolve-SearchExecutable([string]$Requested, [string]$BundleRelative, [bool]$AllowBundled) {
    $command = Get-Command -Name $Requested -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($command) { return $command.Source }
    if ($AllowBundled) {
        $candidate = Join-Path $env:USERPROFILE ".cache/codex-runtimes/codex-primary-runtime/dependencies/$BundleRelative"
        if (Test-Path -LiteralPath $candidate -PathType Leaf) { return [IO.Path]::GetFullPath($candidate) }
    }
    throw "Executable '$Requested' was not found. Specify an existing runtime with -NodePath or -PnpmPath."
}
if ($Setup) {
    $guarded = @((Join-Path $PSScriptRoot '.validation'), $runtime)
    foreach ($name in @('store', 'node_modules', 'package.json', 'pnpm-lock.yaml', 'pnpm-workspace.yaml')) {
        $guarded += Join-Path $runtime $name
    }
    foreach ($path in $guarded) {
        if (Test-Path -LiteralPath $path) {
            if ((Get-Item -LiteralPath $path -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw 'Redirected runtime directories are not supported.'
            }
        }
    }
    $resolvedNode = Resolve-SearchExecutable $NodePath 'node/bin/node.exe' (-not $PSBoundParameters.ContainsKey('NodePath'))
    $resolvedPnpm = Resolve-SearchExecutable $PnpmPath 'bin/fallback/pnpm.cmd' (-not $PSBoundParameters.ContainsKey('PnpmPath'))
    $nodeVersion = & $resolvedNode --version
    if ($LASTEXITCODE -ne 0 -or [version]$nodeVersion.TrimStart('v') -lt [version]'22.0.0') {
        throw 'Local search needs Node.js 22 or later.'
    }
    New-Item -ItemType Directory -Path $runtime -Force | Out-Null
    foreach ($name in @('package.json', 'pnpm-lock.yaml', 'pnpm-workspace.yaml')) {
        Copy-Item -LiteralPath (Join-Path $PSScriptRoot "tools/local_search/$name") -Destination $runtime -Force
    }
    # Explicit opt-in download. No lifecycle scripts, models, global install or hooks.
    $originalPath = $env:Path
    try {
        $env:Path = (Split-Path -Parent $resolvedNode) + [IO.Path]::PathSeparator + $originalPath
        & $resolvedPnpm --dir $runtime install --frozen-lockfile --ignore-scripts --store-dir (Join-Path $runtime 'store')
        $setupExit = $LASTEXITCODE
    } finally { $env:Path = $originalPath }
    exit $setupExit
}
$python = Join-Path $PSScriptRoot '.validation/runtime/venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw 'Run .\Validate-KI-Regeln.ps1 -Quick once to prepare the local Python runtime.'
}
$action = if ($Build) { 'build' } elseif ($Status) { 'status' } elseif ($ListSkills) { 'list-skills' } else { 'search' }
$arguments = @((Join-Path $PSScriptRoot 'tools/search_rules.py'))
if ($PSBoundParameters.ContainsKey('NodePath')) { $arguments += @('--node', $NodePath) }
if ($Routing) { $arguments += '--routing' }
if ($PSBoundParameters.ContainsKey('Limit')) { $arguments += @('--limit', [string]$Limit) }
if ($PSBoundParameters.ContainsKey('Cursor')) { $arguments += "--cursor=$Cursor" }
$arguments += $action
if ($action -eq 'search') { $arguments += @('--', $Query) }
& $python @arguments
exit $LASTEXITCODE
