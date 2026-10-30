[CmdletBinding(DefaultParameterSetName = 'Query')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Query')][string]$Query,
    [Parameter(Mandatory, ParameterSetName = 'Build')][switch]$Build,
    [Parameter(Mandatory, ParameterSetName = 'Status')][switch]$Status,
    [Parameter(Mandatory, ParameterSetName = 'Setup')][switch]$Setup,
    [string]$NodePath = 'node',
    [string]$PnpmPath = 'pnpm'
)
$ErrorActionPreference = 'Stop'
$runtime = Join-Path $PSScriptRoot '.validation/qmd-runtime'
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
    $nodeVersion = & $NodePath --version
    if ($LASTEXITCODE -ne 0 -or [version]$nodeVersion.TrimStart('v') -lt [version]'22.0.0') {
        throw 'Local search needs Node.js 22 or later.'
    }
    New-Item -ItemType Directory -Path $runtime -Force | Out-Null
    foreach ($name in @('package.json', 'pnpm-lock.yaml', 'pnpm-workspace.yaml')) {
        Copy-Item -LiteralPath (Join-Path $PSScriptRoot "tools/local_search/$name") -Destination $runtime -Force
    }
    # Explicit opt-in download. No lifecycle scripts, models, global install or hooks.
    & $PnpmPath --dir $runtime install --frozen-lockfile --ignore-scripts --store-dir (Join-Path $runtime 'store')
    exit $LASTEXITCODE
}
$python = Join-Path $PSScriptRoot '.validation/runtime/venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw 'Run .\Validate-KI-Regeln.ps1 -Quick once to prepare the local Python runtime.'
}
$action = if ($Build) { 'build' } elseif ($Status) { 'status' } else { 'search' }
$arguments = @((Join-Path $PSScriptRoot 'tools/search_rules.py'), '--node', $NodePath, $action)
if ($action -eq 'search') { $arguments += @('--', $Query) }
& $python @arguments
exit $LASTEXITCODE
