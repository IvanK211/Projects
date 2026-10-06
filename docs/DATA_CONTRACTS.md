# Data contracts and interpretation

Use the matching file in `examples/` as the concrete shape. Values and identifiers in these files are synthetic, not a redacted production export. All rate outputs are fractions in the range 0 to 1 where applicable; multiply by 100 only for display. `null` means unavailable or not defined, not zero.

| Workflow | Required input | Important interpretation |
|---|---|---|
| Inventory | Object with `requested` names and `devices` records containing `id`, `deviceName`, optional `lastSyncDateTime` | Exact case-insensitive names; unique IDs; newest/oldest retained for duplicates; null times sort first |
| Comparison | Two arrays with a unique chosen key, default `id` | Added/removed records are snapshot differences, not evidence of a person leaving or an asset being destroyed |
| Training | `users`, explicit `requiredTrainingIds`, `enrollments` with `userId`, `trainingId`, `status` | Active people times requirements is the denominator; completed/passed, incomplete and not-assigned are distinct |
| Phishing | One record per campaign/division with integer `delivered`, `failed`, `reported` | Failures and reports are unique recipients within that campaign, not event counts; overlap between failure and report is permitted |
| PIM | Request objects containing action, status and offset-bearing `createdDateTime` | Self-activation requests are not proof of actual privileged actions; preserve unsuccessful statuses |
| PAM plan | Accounts with unique `id`, address, safe, platform and property map | Suffix uses a DNS-label boundary; planned whole-property update preserves existing values; no live write |
| PAM sessions | Unique recording `id`, `initiatingUser`, start/end timestamps | Attribute use to the initiating identity, not the stored privileged account; missing duration is separately counted |
| Plugins | `pluginId` plus textual name/family/description/CPE metadata | Classification is a heuristic over provided text, not an ID formula or proof of affected assets |
| Risk review | Rule/plugin identifiers plus owner, rationale, reviewDate, expires | Expiry and evidence completeness are independent; accepted rules do not equal instances |
| Sensors | Time, sensor, unit and finite value | Units remain separate; endpoint drift is descriptive, not causal or a calibrated error estimate |
| Logs | Level and eventType, with optional extra private fields | Output excludes raw messages and identities, but custom event names may still disclose information |
| IP correlation | IP, time and observation metadata | Preserve historical candidates; timestamp age, NAT and DHCP prevent a unique present-day identity claim |
| KPIs | Name, unit, numeric `values` and explicit kind sum/mean/last | Values are an already ordered reporting series; unknown values must not be fabricated as zero |

## Collection versus analysis

Provider exports are not guaranteed to match these normalized contracts directly. Adapt field names explicitly, preserve original data in private storage, and validate pagination before analysis. The managed-device collector outputs an array suitable as `devices`; provide the requested-name list separately. PIM collection already emits normalized request fields. A vendor API's nested user object is not interchangeable with a normalized `userId` without an explicit mapping.

Read-only API access may need broad scopes and a supported administrative role. The PIM endpoint's documented permission name includes `ReadWrite` even for this read workflow. The archive does not silently grant consent or assign roles. Group membership type casts use an eventual-consistency header and a count query; results can lag recent changes. See [S02 and S03](SOURCES.md).

## Training period rule

The supplied enrollment array defines the reporting scope. A completion in that array satisfies a required ID. For recurring annual or quarterly obligations, normalize the requirement into a period-specific ID before analysis, or pre-filter both enrollment and requirement sets to the same period. Never allow an old completion to satisfy a new obligation by accident. Changing which people count as active also changes the denominator and must be recorded.

## Weighted rates

A campaign with 40 delivered and 4 failed has a 10% failure rate. Another with 80 delivered and 2 failed has a 2.5% rate. Their recipient-exposure-weighted rate is `(4 + 2) / (40 + 80) = 5%`; their unweighted campaign mean is `(10% + 2.5%) / 2 = 6.25%`. Both are legitimate answers to different questions. Neither is the percentage of distinct people who failed at least once across campaigns. That requires de-duplicated identity-level data, which is not bundled.

## Invalid and incomplete data

Reject duplicate record keys instead of multiplying counts. Correct naive timestamps upstream rather than assuming a timezone. Inspect missing owners, dates and rationales even when a risk has not expired. Do not infer host health from a missing record, infer chemical action from a drift slope, or treat a copied page of API results as a full dataset.

Units for dimensional and hydraulic calculators must be internally consistent. The fit calculator subtracts clearance on both sides of every target axis. Energy input is volts, amp-hours and watts. Flow uses collected liters, collection seconds and reservoir liters. None of these arithmetic models proves electrical, mechanical, crop or chemical safety.
