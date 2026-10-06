# Threat model and safety assumptions

| Boundary or failure | Possible consequence | Mitigation in this edition | Remaining obligation |
|---|---|---|---|
| Live export committed | Identity, asset or policy disclosure | Synthetic fixtures; ignored local-output paths; privacy checks | Review every new file and old Git history |
| Secret printed in error | Exposure through terminal or CI logs | Core CLI prints error class, scanner prints rule locations only | Audit provider SDK errors and operational logs privately |
| Malicious report strings | Script injection when viewing HTML | HTML escaping; snapshot uses textContent; restrictive content policies | Avoid replacing renderer with raw HTML insertion |
| API pagination target changes | Credential sent to another origin | Graph helper restricts HTTPS host and default port; loop/limit guard | Validate sovereign-cloud adapters separately rather than disabling guard |
| Stale property plan | Overwrite another administrator's update | Full-property precondition comparison and re-fetch | Use a change window; residual race exists between read and write |
| Partial change batch | Some accounts updated, others not | Stop on failure; per-item evidence; no false transactional claim | Review and approve drift-aware rollback |
| Watchdog restart loop | Availability disruption | Observation by default, lock and cooldown on apply | Alert humans; do not use restarts as root-cause remediation |
| Unquiesced backup | Unusable database or inconsistent restore | Explicit quiesced-source contract; no automatic live database copy | Execute application-specific backup and isolated restore tests |
| Local controller fault | Dry running, spill or unsafe output | Short bench pulse, level interlock, safe software defaults | Hardware cutoff, correct drivers, electrical protection and supervised test |
| RFID experiment on a real credential | Data damage or unauthorized access | Public UID reading and disabled-by-default data-block lab write | Use disposable owned tags only; no access-control credential experiments |
| Untested mechanical fit | Interference, cracking or heat damage | Arbitrary demonstration dimensions; fit coupons; no certification | Measure, inspect and test the actual application separately |
| Friendly dashboard green despite missing data | False assurance | Unknown/stale states, empty snapshot is unknown, separate liveness/readiness | Independent end-to-end alerts and operational monitoring |

This document identifies design risks, not a completed formal security assessment. Root access, credentials and physical outputs are powerful capabilities. Default examples avoid automatic deployment, broad network listeners, secret ingestion and hazardous output construction. Do not remove those boundaries simply to make a demonstration appear more complete.
