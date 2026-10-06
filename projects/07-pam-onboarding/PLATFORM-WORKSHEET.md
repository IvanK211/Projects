# PAM platform onboarding worksheet

## Scope and ownership

Record a fictional reference identifier, platform category, connection method, accountable reviewer and test objective. Keep live safe names, account names, host lists and policy IDs in a separate private change record.

## Credential lifecycle

Define discovery, onboarding, verification, change, reconciliation, dependency handling, checkout, session initiation and retirement as separate functions. Identify which function a connector actually implements. A working browser session is not proof that automated password rotation is supported.

## Access model

Separate account discovery/read, secret retrieval, session initiation, account modification, safe administration and monitoring access. Test a least-privileged identity and an intentionally denied identity. Do not use a broad administrator role to prove a delegated policy works.

## Session path

Verify browser and driver compatibility, target certificate trust, DNS resolution, proxy/load-balancer behavior, authentication redirects and required isolation. Compare a direct lab connection with the mediated session path without bypassing production controls. Preserve error codes and stage names privately; do not publish recordings.

## Acceptance and recovery

Require a successful allowed connection, denied unauthorized connection, correct audit attribution, tested credential change where supported, recovery of the previous working configuration and an approved maintenance owner. Mark unsupported functions explicitly. Stop after an unexplained credential change or mismatch between the expected and observed target.
