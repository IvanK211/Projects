#requires -Version 7.2
<#
.SYNOPSIS
Exports directory-role selfActivate requests after an explicit timestamp.
.DESCRIPTION
Keeps successful, failed and pending statuses distinct. Does not cover Azure RBAC or
PIM for Groups. The documented endpoint requires a ReadWrite-named OAuth scope even
though this script performs GET requests only. Name resolution is optional and broader.
#>
[CmdletBinding()]
param([Parameter(Mandatory)][string]$TenantId,
      [Parameter(Mandatory)][DateTimeOffset]$SinceUtc,
      [string]$OutputPath='./local-output/pim-requests.json',
      [switch]$ResolveNames, [switch]$UseDeviceCode)
$ErrorActionPreference='Stop'
Import-Module Microsoft.Graph.Authentication -ErrorAction Stop
Import-Module (Join-Path $PSScriptRoot '../../powershell/GraphRead.psm1') -Force
$scopes=@('RoleAssignmentSchedule.ReadWrite.Directory')
if ($ResolveNames) { $scopes += 'Directory.Read.All' }
$connect=@{TenantId=$TenantId;Scopes=$scopes;ContextScope='Process';NoWelcome=$true}
if ($UseDeviceCode) { $connect.UseDeviceCode=$true }
try {
    Connect-MgGraph @connect | Out-Null
    $select='id,principalId,roleDefinitionId,action,status,createdDateTime,completedDateTime,justification,scheduleInfo,ticketInfo,directoryScopeId'
    $uri="https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests?`$select=$select"
    # Filter locally to avoid depending on a server-side combined filter implementation.
    $all=@(Get-GraphPages -Uri $uri)
    $users=@{}; $roles=@{}; $unresolved=0
    $rows=[System.Collections.Generic.List[object]]::new()
    foreach ($request in $all) {
        if ((Get-OptionalProperty $request 'action') -ne 'selfActivate') { continue }
        $createdText=[string](Get-OptionalProperty $request 'createdDateTime')
        if (-not $createdText) { continue }
        $created=[DateTimeOffset]::Parse($createdText)
        if ($created -lt $SinceUtc) { continue }
        if ($ResolveNames) {
            foreach ($kind in @('User','Role')) {
                $id=if ($kind -eq 'User') { [string]$request.principalId } else { [string]$request.roleDefinitionId }
                $cache=if ($kind -eq 'User') { $users } else { $roles }
                if (-not $cache.ContainsKey($id)) {
                    $encoded=[uri]::EscapeDataString($id)
                    $endpoint=if ($kind -eq 'User') { "users/$encoded" } else { "roleManagement/directory/roleDefinitions/$encoded" }
                    try { $cache[$id]=Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/$endpoint" -OutputType PSObject }
                    catch { $cache[$id]=$null; $unresolved++ }
                }
            }
            $upn=Get-OptionalProperty $users[[string]$request.principalId] 'userPrincipalName'
            $roleName=Get-OptionalProperty $roles[[string]$request.roleDefinitionId] 'displayName'
            $request | Add-Member -NotePropertyName resolvedUserPrincipalName -NotePropertyValue $upn -Force
            $request | Add-Member -NotePropertyName resolvedRoleName -NotePropertyValue $roleName -Force
        }
        $rows.Add($request)
    }
    Save-PrivateJson -Data @($rows.ToArray()) -Path $OutputPath
    Write-Host "Exported $($rows.Count) requests; unresolved lookups: $unresolved."
} finally { Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null }
