# Delivered evidence / expanded v2

`qualification.json` describes this source set. NOT_RUN is never PASS.
Current reports are in `assurance/evidence/current-reference-checks.json` and
`current-source-checks.json`. Independent Python/native probes and static source checks
were performed; the Ada executables and GNATprove were NOT run.

The original preparation environment had no gnat1/GPRbuild/GNATprove. Current tool
preflights confirm GPRbuild is absent; they are not a compilation attempt. Old results
under `history-v1/` are historical only and must not qualify the current code.

`ci/verify.sh` creates a fresh private evidence directory for a later user-run build,
tests and GNATprove. It never rewrites historical delivery evidence or silently promotes
the source to production. Bind any new results to the exact source/compiler/native-library
identities and record site integration and fault tests independently.
