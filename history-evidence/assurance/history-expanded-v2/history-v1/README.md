# Evidence status

The supplied `qualification.json` reports the state of this delivered archive.
`NOT_RUN` is not `PASS`. Logs under the assurance repository distinguish executed
independent reference checks from Ada execution, which was unavailable.

`ci/verify.sh` generates a fresh private result directory and records its path in
`latest-run-path.txt`. It never promotes this release to production and never rewrites
historical delivery evidence. Preserve the directory and bind it to a source digest
before using the results in an independent assessment.
