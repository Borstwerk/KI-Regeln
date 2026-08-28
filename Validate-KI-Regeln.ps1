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

# Keep repository validation read-only: repository Python imports must not create __pycache__ files.
$env:PYTHONDONTWRITEBYTECODE = '1'

$corePath = Join-Path $PSScriptRoot 'Validate-KI-Regeln.Core.ps1'
if (-not (Test-Path -LiteralPath $corePath)) {
    Write-Error 'Local validation core script is missing: Validate-KI-Regeln.Core.ps1'
    exit 2
}

$invokeArgs = @{}
if ($Quick) { $invokeArgs.Quick = $true }
if ($Full) { $invokeArgs.Full = $true }
if ($Release) { $invokeArgs.Release = $true }
if ($WarningsAsErrors) { $invokeArgs.WarningsAsErrors = $true }
if ($NoBootstrap) { $invokeArgs.NoBootstrap = $true }

& $corePath @invokeArgs
exit $LASTEXITCODE
