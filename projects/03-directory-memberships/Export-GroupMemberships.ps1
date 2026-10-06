#requires -Version 7.2
[CmdletBinding()]
param([Parameter(Mandatory)][string]$TenantId,
      [Parameter(Mandatory)][string]$UserIdsJson,
      [string]$GroupPrefix='', [switch]$Transitive,
      [string]$OutputPath='./local-output/group-memberships.json')
$ErrorActionPreference='Stop'
Import-Module Microsoft.Graph.Authentication -ErrorAction Stop
Import-Module (Join-Path $PSScriptRoot '../../powershell/GraphRead.psm1') -Force
$ids=@(Get-Content -Raw -LiteralPath $UserIdsJson | ConvertFrom-Json)
try {
    Connect-MgGraph -TenantId $TenantId -Scopes 'Directory.Read.All' -ContextScope Process -NoWelcome | Out-Null
    $rows=@(foreach ($id in $ids) {
        if ([string]::IsNullOrWhiteSpace([string]$id)) { throw 'Empty user ID.' }
        $relation=if ($Transitive) { 'transitiveMemberOf' } else { 'memberOf' }
        $encoded=[uri]::EscapeDataString([string]$id)
        $uri="https://graph.microsoft.com/v1.0/users/$encoded/$relation/microsoft.graph.group?`$select=id,displayName&`$count=true"
        $groups=@(Get-GraphPages -Uri $uri -Headers @{ConsistencyLevel='eventual'} | Where-Object {
            $name=[string](Get-OptionalProperty $_ 'displayName' '')
            -not $GroupPrefix -or $name.StartsWith($GroupPrefix,[StringComparison]::OrdinalIgnoreCase)
        })
        [pscustomobject]@{userId=$id;relation=$relation;groups=$groups;groupCount=$groups.Count}
    })
    Save-PrivateJson -Data $rows -Path $OutputPath
} finally { Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null }
