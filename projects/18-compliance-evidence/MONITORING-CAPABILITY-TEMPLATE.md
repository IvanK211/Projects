# Monitoring-capability statement template

For the approved scope, describe the telemetry sources, collection route, parsing and normalization, time synchronization, detection use cases, triage ownership, escalation path, response procedures and review process.

Specify coverage gaps, unsupported systems, retention limits, clock uncertainty and delayed sources. Distinguish deployment from operational testing: an agent installed on an endpoint does not prove ingestion, detection, alert routing and human response all work.

Use one authorized synthetic event to test the full path. Record stage timestamps privately and verify that the event is correctly attributed and escalated. Repeat after material changes. Publish only the generic method, not rule details, detection blind spots or actual response performance.

Avoid absolute phrases such as all systems, real-time protection, fully compliant or zero risk unless a narrowly defined, independently supported claim justifies them.
