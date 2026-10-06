#requires -Version 7.2
<#
.SYNOPSIS
Read-only Microsoft Graph managed-device inventory export. Live data stays local.
.DESCRIPTION
Requires Microsoft.Graph.Authentication, an active Intune license and approved consent.
Assigned user fields are not proof of asset ownership. No automatic module installation.
#>
[CmdletBinding()]
param([Parameter(Mandatory)][string]$TenantId,
      [string]$OutputPath = './local-output/managed-devices.json', [switch]$UseDeviceCode)
$ErrorActionPreference = 'Stop'
Import-Module Microsoft.Graph.Authentication -ErrorAction Stop
Import-Module (Join-Path $PSScriptRoot '../../powershell/GraphRead.psm1') -Force
$connect = @{TenantId=$TenantId; Scopes=@('DeviceManagementManagedDevices.Read.All'); ContextScope='Process'; NoWelcome=$true}
if ($UseDeviceCode) { $connect.UseDeviceCode = $true }
try {
    Connect-MgGraph @connect | Out-Null
    $select = 'id,deviceName,operatingSystem,osVersion,userDisplayName,userPrincipalName,lastSyncDateTime,managedDeviceOwnerType'
    $uri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?`$select=$select"
    $devices = @(Get-GraphPages -Uri $uri)
    Save-PrivateJson -Data $devices -Path $OutputPath
    Write-Host "Exported $($devices.Count) records. Keep the output private."
} finally { Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null }
