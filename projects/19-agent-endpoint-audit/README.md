# Region-aware agent and API endpoint review

**Category:** Infrastructure and operations  
**Archive status:** Offline transformation tool + connectivity runbook

This is a generic reference edition, not an export or description of an actual deployment. Status refers to the files in this archive, not a claim about a private system.

## Purpose

Find and propose exact endpoint-host replacements without blindly rewriting software configuration or assuming all regional URLs follow the same pattern.

## Design and behavior

The tool applies an explicit hostname map to URL tokens, preserves paths and queries, refuses embedded credentials and writes only a new file when --write-copy is supplied. The default run is a summary-only review. JumpCloud is a reference use case, but actual service endpoint inventories and region choices are deliberately absent.

## Included implementation

- [labkit/endpoints.py](../../labkit/endpoints.py)
- [projects/19-agent-endpoint-audit/prepare_endpoint_copy.py](../../projects/19-agent-endpoint-audit/prepare_endpoint_copy.py)
- [examples/endpoint-map.json](../../examples/endpoint-map.json)
- [examples/endpoint-input.txt](../../examples/endpoint-input.txt)

## Reference entry point

Run from the repository root. Commands using `examples/` use newly created synthetic data. Other commands may inspect the local machine or start a loopback-only demo; read the script first.

```sh
python projects/19-agent-endpoint-audit/prepare_endpoint_copy.py examples/endpoint-input.txt examples/endpoint-map.json local-output/endpoint-copy.txt
```

## Workflow

1. Verify the provider-specific portal, API, authentication and agent endpoints in current documentation.

2. Build a local mapping of only the exact approved hostnames; do not use a universal domain string replacement.

3. Run the review, then create a new protected copy with --write-copy and inspect the complete file privately.

4. Use a vendor-supported migration or repair procedure for installed agents; this tool never modifies an agent in place or migrates an organization between regions.

## Acceptance criteria

- Unrelated URLs are unchanged.
- The original file is never overwritten.
- Only hostnames are counted in diagnostics; URL queries and credentials are not printed.

## Troubleshooting and limits

A working portal login does not establish the correct API or OAuth issuer.

HTTP 401/403 responses are not necessarily network failures.

Changing a URL is not equivalent to migrating a provider organization.

## Publication boundary

Keep live inputs, outputs, credentials, screenshots, configuration exports and environment-specific changes in a separate private workspace. A successful local unit test does not establish vendor API compatibility, hardware safety, production readiness or permission to publish work-owned material.

## Technical references

[S11](../../docs/SOURCES.md#s11). The linked vendor/reference documentation supports platform details; the workflow and test choices here are original reference design decisions.

See [RUNBOOK.md](RUNBOOK.md), [validation evidence](../../docs/VALIDATION.md), and [the privacy model](../../docs/PRIVACY.md).
