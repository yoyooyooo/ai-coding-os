# Atomic Patch Protocol

The Kit performs all conflict, schema, path, and profile checks before writing
project source. It stages a complete patch, validates it, then commits with a
lock and rollback journal.

No command may return failure after intentionally leaving source/registry/
manifest in mismatched state. Expected commit failures return structured JSON
with `error_code`, `rolled_back`, and `message`; the lock is released, temporary
staging is removed, and a crash/rollback journal is retained for `repair` or
audit inspection. Raw tracebacks are reserved for defects outside the expected
machine contract.

Managed files may be regenerated. User-owned capability files are create-only
unless a future explicit migration operation states otherwise.
