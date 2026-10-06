#requires -Version 7.2
<#
.SYNOPSIS
Reviews or applies an offline labkit PAM port plan. No changes without -Apply.
.DESCRIPTION
Re-fetches each account, verifies scope and complete platform-property preconditions,
updates only the intended property, and re-fetches for verification. Stops on any failure.
Not transactional: prior successful changes remain and require manual rollback review.
#>
[CmdletBinding(SupportsShouldProcess=$true,ConfirmImpact='High')]
param([Parameter(Mandatory)][uri]$BaseUrl,
      [Parameter(Mandatory)][string]$PlanPath,
      [ValidateSet('CyberArk','LDAP','Radius')][string]$AuthType='CyberArk',
      [ValidateRange(1,100)][int]$MaxChanges=10,
      [switch]$Apply,
      [string]$OutputPath='./local-output/pam-apply-results.json')
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
Import-Module (Join-Path $PSScriptRoot '../../powershell/GraphRead.psm1') -Force
if ($BaseUrl.Scheme -ne 'https' -or $BaseUrl.UserInfo -or $BaseUrl.Query -or $BaseUrl.Fragment) { throw 'Use an HTTPS base URL without credentials/query/fragment.' }
$base=$BaseUrl.AbsoluteUri.TrimEnd('/')
if ($base -notmatch '/PasswordVault$') { $base += '/PasswordVault' }
$plan=Get-Content -LiteralPath $PlanPath -Raw | ConvertFrom-Json
if ($plan.mode -ne 'plan-only') { throw 'Unexpected plan mode.' }
$suffix=([string]$plan.suffix).Trim().TrimStart('.').TrimEnd('.').ToLowerInvariant()
if ($suffix -notmatch '^[a-z0-9][a-z0-9.-]*\.[a-z0-9][a-z0-9.-]*$' -or $suffix.Contains('..')) { throw 'Invalid plan suffix.' }
foreach ($row in @($plan.accounts)) {
    $address=([string]$row.address).Trim().TrimEnd('.').ToLowerInvariant()
    if ($address -ne $suffix -and -not $address.EndsWith('.'+$suffix,[StringComparison]::Ordinal)) { throw 'Account outside planned suffix.' }
    if ([int]$row.newPort -ne [int]$plan.newPort) { throw 'Inconsistent target port in plan.' }
}

$changes=@($plan.accounts | Where-Object action -eq 'review')
if ($changes.Count -gt $MaxChanges) { throw 'Change limit exceeded; review and split the plan.' }
if (@($changes.accountId | Select-Object -Unique).Count -ne $changes.Count) { throw 'Duplicate account IDs.' }
if (-not $Apply) { Write-Host "Review only: $($changes.Count) proposed updates. No network calls made."; return }
function PropertyMap($obj) {
    $result=[ordered]@{}
    if ($null -ne $obj) {
        foreach ($property in @($obj.PSObject.Properties | Sort-Object Name)) { $result[$property.Name]=$property.Value }
    }
    return (ConvertTo-Json -InputObject $result -Depth 20 -Compress)
}
function Call-Pam([string]$Method,[string]$Path,$Body=$null) {
    $args=@{Method=$Method;Uri="$base/$Path";ContentType='application/json';MaximumRedirection=0;TimeoutSec=30}
    if ($script:token) { $args.Headers=@{Authorization=$script:token} }
    if ($null -ne $Body) { $args.Body=$Body }
    Invoke-RestMethod @args
}
$script:token=$null
$results=[System.Collections.Generic.List[object]]::new()
try {
    $credential=Get-Credential -Message 'Approved PAM lab credentials'
    if ($null -eq $credential) { throw 'Authentication cancelled.' }
    $login=@{username=$credential.UserName;password=$credential.GetNetworkCredential().Password} | ConvertTo-Json -Compress
    $script:token=Call-Pam 'POST' "API/Auth/$AuthType/Logon" $login
    $login=$null; $credential=$null
    foreach ($change in $changes) {
        $id=[uri]::EscapeDataString([string]$change.accountId)
        $current=Call-Pam 'GET' "API/Accounts/$id/"
        if ($current.address -ne $change.address -or $current.safeName -ne $change.safeName -or $current.platformId -ne $change.platformId) { throw 'Account scope drift; regenerate plan.' }
        $before=Get-OptionalProperty $current 'platformAccountProperties' ([pscustomobject]@{})
        if ((PropertyMap $before) -cne (PropertyMap $change.beforeProperties)) { throw 'Property drift; regenerate plan.' }
        $port=[int]$change.newPort
        if ($port -lt 1 -or $port -gt 65535) { throw 'Invalid port.' }
        $after=[ordered]@{}
        foreach ($property in $before.PSObject.Properties) { $after[$property.Name]=$property.Value }
        $keys=@($after.Keys | Where-Object { $_ -ieq 'port' })
        if ($keys.Count -gt 1) { throw 'Ambiguous port casing.' }
        $key=if ($keys.Count) { [string]$keys[0] } else { 'Port' }
        $after[$key]=[string]$port
        # Do not trust executable PATCH content from the input plan: construct it here.
        $operation=@{op='add';path='/platformaccountproperties';value=$after}
        $body=ConvertTo-Json -InputObject @($operation) -Depth 20 -Compress
        if ($PSCmdlet.ShouldProcess('Reviewed account record','Update port property')) {
            Call-Pam 'PATCH' "API/Accounts/$id/" $body | Out-Null
            $verified=Call-Pam 'GET' "API/Accounts/$id/"
            $actual=Get-OptionalProperty (Get-OptionalProperty $verified 'platformAccountProperties') $key
            if ([string]$actual -ne [string]$port) { throw 'Post-update verification failed.' }
            $results.Add([pscustomobject]@{accountId=$change.accountId;status='verified';oldPort=$change.oldPort;newPort=$port})
            Save-PrivateJson -Data @($results.ToArray()) -Path $OutputPath
        }
    }
} catch { throw 'PAM operation stopped. Inspect private audit output and provider logs; do not publish response bodies.' }
finally {
    if ($script:token) { try { Call-Pam 'POST' 'API/Auth/Logoff' | Out-Null } catch { Write-Warning 'Logoff failed; allow the session to expire or revoke it privately.' } }
    $script:token=$null
}
