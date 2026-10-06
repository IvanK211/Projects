# PAM property-change recovery

This executor is not transactional. A later failure does not reverse earlier writes. A client timeout also does not prove that the server failed to apply a write.

## Before applying

Keep the reviewed plan and complete original property maps in private, access-controlled storage. Confirm the exact DNS suffix, safe/platform scope, count and target port. Test one disposable lab account first. Record the platform's field casing and accepted update shape. Maintain a separate recovery access path.

## After an interruption

Stop the batch. Re-fetch every account attempted since the last confirmed result. Classify each as unchanged, expected new state, unexpectedly changed or unresolvable. Do not infer account state solely from the local log or process exit code. Keep evidence private.

## Reversal decision

For an account in the exact expected new state, a reviewer may approve restoring the original property map. Compare the current map with the previously approved after-state immediately before reversal. If another administrator changed any value, stop and resolve the conflict rather than replacing their work. Use the vendor-supported property update interface; do not edit a vault database.

Re-fetch after each approved reversal. Validate both the property and a controlled connection when authorized. Record attempted, applied, verified, unverified and skipped states separately. A restored port setting does not automatically restore sessions or external services. Close the change only after the target state is independently verified.
