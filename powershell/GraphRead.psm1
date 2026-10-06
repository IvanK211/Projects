#requires -Version 7.2
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
function Get-OptionalProperty {
    param($Object, [string]$Name, $Default = $null)
    if ($null -ne $Object -and $null -ne $Object.PSObject.Properties[$Name]) {
        return $Object.PSObject.Properties[$Name].Value
    }
    return $Default
}
function Get-GraphPages {
    [CmdletBinding()]
    param([Parameter(Mandatory)][uri]$Uri, [ValidateRange(1,10000)][int]$MaxPages = 1000, [hashtable]$Headers = @{})
    $next = $Uri.AbsoluteUri
    $seen = [System.Collections.Generic.HashSet[string]]::new()
    $items = [System.Collections.Generic.List[object]]::new()
    while ($next) {
        $parsed = [uri]$next
        if ($parsed.Scheme -ne 'https' -or $parsed.Host -ne 'graph.microsoft.com' -or
            -not $parsed.IsDefaultPort -or $parsed.UserInfo) { throw 'Untrusted pagination URL.' }
        if (-not $seen.Add($next) -or $seen.Count -gt $MaxPages) { throw 'Pagination loop/limit.' }
        # Graph SDK applies its own HTTP retry handling. Do not print raw response bodies.
        $page = Invoke-MgGraphRequest -Method GET -Uri $next -Headers $Headers -OutputType PSObject
        $valueProperty = $page.PSObject.Properties['value']
        if ($null -eq $valueProperty -or $null -eq $valueProperty.Value) { throw 'Unexpected Graph response envelope.' }
        foreach ($item in @($valueProperty.Value)) { $items.Add($item) }
        $next = [string](Get-OptionalProperty $page '@odata.nextLink' '')
    }
    return $items.ToArray()
}
function Save-PrivateJson {
    param([Parameter(Mandatory)]$Data, [Parameter(Mandatory)][string]$Path)
    $full = [IO.Path]::GetFullPath($Path)
    $parent = Split-Path -Parent $full
    [IO.Directory]::CreateDirectory($parent) | Out-Null
    # Restrict the destination folder with OS ACLs before collecting live data.
    $temp = Join-Path $parent ([IO.Path]::GetRandomFileName())
    try {
        ConvertTo-Json -InputObject $Data -Depth 30 | Set-Content -LiteralPath $temp -Encoding utf8
        Move-Item -LiteralPath $temp -Destination $full -Force
    } finally { if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp } }
}
Export-ModuleMember -Function Get-GraphPages,Get-OptionalProperty,Save-PrivateJson
