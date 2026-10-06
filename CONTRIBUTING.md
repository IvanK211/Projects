# Contributing

Keep the collection a public reference, not an operational repository. Add only independently invented data. Never copy a private configuration and replace two hostnames while leaving the rest intact. Update the project status when code changes from a concept to an implementation or when a new validation is actually performed.

A change should include its problem statement, input contract, limitations, expected outputs, negative tests and review of publication rights. Run the privacy scan, structure check, unit tests and demo. For shell, PowerShell, KQL, firmware and infrastructure files, state which interpreter, API or hardware checks were not performed. Do not claim integration coverage from a syntax parser alone.

Avoid dependencies unless they materially improve the project. Keep imports explicit, avoid automatic package installation, preserve TLS verification and use read-only permissions where the platform permits them. Live mutation must require explicit operator action, bounded scope, reviewed preconditions and a recovery plan. Keep logs and detailed errors private.

Update `PROJECTS.md`, `project-catalog.json`, the affected `project.json`, relevant source references and `docs/VALIDATION.md`. Then run `python tools/build_index.py`. The generated release manifest is refreshed by the packaging tool, not edited by hand.
