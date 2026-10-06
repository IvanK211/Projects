# Reference architecture

## Separation of concerns

The collection has four intentionally separate layers. The `labkit` package transforms normalized local data. Project-specific PowerShell or shell files demonstrate optional boundary integrations. Project documentation explains interpretation, operating risks and prerequisites. Repository tools validate and package the public edition. No shared configuration joins these layers to a real organization or household.

```text
Fictional fixtures -> pure transformation -> local result -> human interpretation

Private live system -> separately approved collector -> PRIVATE normalized data
                                             |
                                      same pure transform
                                             |
                                      PRIVATE local result
```

The bottom path is a future controlled adaptation, not something executed during preparation of this archive. The default demo follows only the top path.

## Data and failure behavior

JSON is the core interchange format. It avoids spreadsheet formula execution and can be validated without office applications. Runtime reports may still contain sensitive information and are not publication-safe merely because their format is JSON. Every CLI requires a separate output path; it refuses to overwrite the resolved input path. Atomic JSON writes prevent partially written output from replacing a previous result.

Inputs are bounded by a 20 MiB file limit. Numeric helpers reject booleans, non-finite values and invalid nonnegative counts where those restrictions are meaningful. Timestamp-bearing workflows require an explicit offset and compare values in UTC. Missing denominators and first telemetry samples remain `null` rather than being silently turned into zero.

PAM property planning is an offline step. The separate apply template is not transactional. It re-fetches scope and full property preconditions before each write, requires an explicit apply switch, limits change count and checks the updated port. A failed batch may contain prior successful changes. Human-approved, drift-aware recovery is required; do not advertise a batch as all-or-nothing.

## Trust boundaries

Input files are untrusted. HTML output escapes supplied strings, the local snapshot viewer renders with `textContent`, and neither performs templated shell execution. PowerShell Graph pagination restricts the destination to its intended public Graph host. Region changes are proposed into a new file using an explicit hostname map, never guessed from a geographic suffix.

User-supplied runtime configuration is private. Credentials are not stored in examples. Automatic credential discovery, silent module installation, broad TLS-verification bypasses, automatic live deployment and public management listeners are intentionally absent from the core workflows.

## Reuse and modularity

A monorepo preserves shared utilities, tests and consistent documentation while making individual topics easy to browse. Extracting a project into its own repository requires retaining the package modules or shared PowerShell helpers it imports, its relevant fixtures, its validation instructions and the publication notices. The source inventory makes dependencies visible; do not copy only a launcher and assume it is standalone.

## Limits

This is not a SIEM deployment, monitoring SLA, turnkey PAM connector, complete data warehouse, qualified electrical design or certified controller. It is a reference implementation and documentation collection. API retention, authorization, billing, schema differences, region support and hardware electrical characteristics remain properties of the destination platform and must be checked there.
