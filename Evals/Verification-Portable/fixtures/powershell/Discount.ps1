function Get-DiscountedPrice {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][decimal]$Price,
        [Parameter(Mandatory = $true)][decimal]$Rate
    )
    if ($Price -lt 0) { throw 'Price must be nonnegative.' }
    if ($Rate -lt 0 -or $Rate -gt 1) { throw 'Rate must be between 0 and 1.' }
    return [decimal]::Round(($Price * (1 - $Rate)), 2, [MidpointRounding]::AwayFromZero)
}
