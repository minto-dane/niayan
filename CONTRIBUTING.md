# Contributing

Start with [STATUS.ja.md](STATUS.ja.md) and [development instructions](dev/README.ja.md). Keep changes within the owning component; the workspace records the tested combination of commits.

Project-authored contributions use BSD-3-Clause. Preserve existing copyright
attribution and identify third-party imports with their original notices; see
[LICENSING.md](LICENSING.md). Run `make license-check` before publishing.

1. Create a branch in the component repository. Preserve its public contracts, bounded inputs and fail-closed behavior.
2. Add a regression test for a behavioral fix. Register every Ada test main in `assurance/engineering/test-plan.json` and regenerate component runners with `python3 assurance/ci/sync-component-ci.py --write`.
3. Update affected requirements, hazards, fault cases and the ADR when changing a contract. Shared source changes must use the documented vendor/profile regeneration tools.
4. Run `make check`, `make private-dbus` and the affected strict `make flow prove` checks. Changes to build settings also require `make reproducible`. Report failures and untested external integrations explicitly.
5. Commit changes in the component first, then commit its submodule pointer in the workspace. Do not edit generated vendor files or rewrite imported evidence to make checks pass.

Each component CI compiles every unit, links its applications, runs all registered Ada tests and runs strict SPARK verification separately. Workspace CI validates cross-component contracts and the private test bus. A successful native job does not replace a failing proof job.

Never commit production credentials or signing keys. Existing deterministic fixture keys are public test material, not deployment credentials. No production installation or live service mutation is part of the default test commands.
