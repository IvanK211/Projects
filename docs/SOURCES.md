# Primary sources

Public references used to check interface and design details during preparation of this edition. They are not private project evidence. Links containing current or latest do not identify a deployed version. Follow the vendor documentation for the destination before integration. Review date: 2026-10-06.

## S01

**Microsoft Graph managed-device listing.** [Official reference](https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-list?view=graph-rest-1.0). Managed-device endpoint and read permissions; validate licensing and supported fields in the destination.

## S02

**Microsoft Graph directory-role schedule requests.** [Official reference](https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roleassignmentschedulerequests?view=graph-rest-1.0). Request scope, fields and documented permissions. The read workflow still uses a permission whose name includes ReadWrite; no role assignment is performed by this collector.

## S03

**Microsoft Graph direct group memberships.** [Official reference](https://learn.microsoft.com/en-us/graph/api/user-list-memberof?view=graph-rest-1.0). Membership semantics and advanced-query requirements. Type casts require eventual consistency and a count query; recently changed membership can lag.

## S04

**Microsoft Defender DeviceNetworkInfo schema.** [Official reference](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkinfo-table). Network adapter observations and IPAddresses JSON-string semantics. Example queries parse before expanding.

## S05

**CyberArk account update API.** [Official reference](https://docs.cyberark.com/pam-self-hosted/latest/en/content/sdk/updateaccount%20v10.htm). Account update shape and JSON patch array. Validate property names against the selected platform rather than trying speculative live payload variants.

## S06

**Tenable Security Center accepted-risk rules.** [Official reference](https://docs.tenable.com/security-center/api/Accept-Risk-Rule.htm). Accepted-risk-rule API resource and rule identifiers. Rule records must not be confused with underlying vulnerability instances or plugin IDs.

## S07

**KnowBe4 Reporting API overview.** [Official reference](https://support.knowbe4.com/hc/en-us/articles/115016090908-Reporting-API-Overview). Reporting API data categories, authentication and access availability. This archive implements normalized offline analysis rather than a live reporting API client.

## S08

**Python HTML escaping.** [Official reference](https://docs.python.org/3/library/html.html). The html.escape function used to render untrusted values as text in standalone reports.

## S09

**Wazuh server API documentation.** [Official reference](https://documentation.wazuh.com/current/user-manual/api/index.html). Integration starting point for a future authorized collector. The included dashboard reads local snapshots and is not a live Wazuh adapter.

## S10

**Microsoft endpoint DLP and Conditional Access.** [Official reference](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about). Endpoint DLP overview. Policy scope and feature support must be verified in the destination.

## S11

**JumpCloud data centers and endpoints.** [Official reference](https://jumpcloud.com/support/jumpcloud-data-centers-login-urls-and-service-endpoints). Public regional endpoint reference. The offline hostname mapper requires an explicit approved map and does not guess production endpoints.

## S12

**systemd timer manual.** [Official reference](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html). Timer activation semantics, interval configuration and the distinction between service state and scheduled activation.

## S13

**Docker Compose interpolation.** [Official reference](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/). Required variable syntax and configuration interpolation. Resolved configuration can expose local values and should remain private.

## S14

**age upstream documentation.** [Official reference](https://github.com/FiloSottile/age/blob/main/README.md). Recipient-based encryption and identity-based decryption. The archive contains neither recipients nor private identities.

## S15

**Eclipse Mosquitto configuration manual.** [Official reference](https://mosquitto.org/man/mosquitto-conf-5.html). Authentication and topic ACL configuration. Validate the chosen broker image and file permissions before starting it.

## S16

**Home Assistant automation triggers.** [Official reference](https://www.home-assistant.io/docs/automation/trigger/). State triggers and timing semantics. A for-duration is not durable across an automation reload or application restart.

## S17

**ESPHome switch component.** [Official reference](https://esphome.io/components/switch/). Software restore modes such as ALWAYS_OFF. Software defaults do not replace an independent hardware safety mechanism.

## S18

**Penn State Extension irrigation-water tests.** [Official reference](https://extension.psu.edu/interpreting-irrigation-water-tests). Water-property interpretation and the need to distinguish individual measurements. No chemical dosing prescription is included.

## S19

**MFRC522 upstream Arduino library.** [Official reference](https://github.com/miguelbalboa/rfid). SPI reader library and hardware reference. The library is not vendored and the sketches require a separately reviewed installation.

## S20

**Arduino millis reference.** [Official reference](https://docs.arduino.cc/language-reference/en/functions/time/millis/). Timer API reference for nonblocking sketches. Unsigned elapsed-time arithmetic is used; physical timing and board behavior still need testing.

## S21

**OpenSCAD documentation.** [Official reference](https://openscad.org/documentation.html). Modeling language and rendering reference. Geometry in this archive is newly authored with arbitrary dimensions.

## S22

**GitLab projects and publishing.** [Official reference](https://docs.gitlab.com/user/project/working_with_projects/). Project creation and repository operations; no GitLab account was accessed or modified to prepare this archive.

## Additional references

[KnowBe4 developer reference](https://developers.knowbe4.com/rest/reporting/) covers provider-specific schemas and regional base URLs.

[Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) and [emergency-access guidance](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) support the rollout design, not a claim of deployed policy.

[GitLab secret push protection](https://docs.gitlab.com/user/application_security/secret_detection/secret_push_protection/) describes a native feature whose availability and configuration must be checked for the destination offering. It is separate from this repository's local heuristic scanner.

This collection links to public documentation rather than redistributing manuals. No vendor approval, compatibility certification or entitlement is implied.
