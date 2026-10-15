$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Discount.ps1')
function Assert-EqualDecimal {
    param([decimal]$Expected, [decimal]$Actual, [string]$Case)
    if ($Expected -ne $Actual) {
        throw ("{0}: expected {1}, observed {2}" -f $Case, $Expected, $Actual)
    }
}
Assert-EqualDecimal 80 (Get-DiscountedPrice -Price 100 -Rate 0.2) 'ordinary discount'
Assert-EqualDecimal 0 (Get-DiscountedPrice -Price 0 -Rate 0.2) 'zero'
Assert-EqualDecimal 10 (Get-DiscountedPrice -Price 19.99 -Rate 0.5) 'rounding'
Assert-EqualDecimal 0 (Get-DiscountedPrice -Price 125 -Rate 1) 'full discount'
$threw = $false
try {
    Get-DiscountedPrice -Price 1 -Rate 1.2 | Out-Null
} catch {
    $threw = $true
}
if (-not $threw) { throw 'Invalid rate was not rejected.' }
Write-Output 'NATIVE_POWERSHELL_ASSERTIONS_PASS'
