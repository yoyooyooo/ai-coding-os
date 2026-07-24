# Atomic Patch Protocol

The Kit performs all conflict, schema, path, and profile checks before writing
project source. It stages a complete patch, validates it, then commits with a
lock and rollback journal.

No command may return failure after intentionally leaving source/registry/
manifest in mismatched state. A crash journal is retained for `repair` to
inspect.

Managed files may be regenerated. User-owned capability files are create-only
unless a future explicit migration operation states otherwise.
