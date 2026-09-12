# niayan

Public OS name: **niayan**. Nia remains the internal component architecture. See [production work](PRODUCTION.ja.md) for the remaining release gates. Existing storage identifiers and historical evidence retain their original names.

niayan is a Debian 13 Linux distribution under development, built around the Nia components. This workspace pins seven independent Ada/SPARK component repositories and the distribution specification repository as Git submodules. [日本語](README.ja.md).

The active task is [complete replacement of APT/dpkg by Nia](distribution/native/README.ja.md),
with [desktop-compatible hardening](distribution/hardening/README.ja.md).
The accepted image below remains the earlier APT-based reference, not a completed native replacement.

**Bootable, installable Debian 13 KDE development image; not production qualified.** The actual ISO passed BIOS, UEFI, Secure Boot, Japanese input, offline/online installation and reboot, and signed APT metadata retrieval in bounded VMs. Two independent ISO builds match byte for byte, and the corresponding source archives have been collected and verified after copying. See the [distribution acceptance](distribution/evidence/debian13/accepted-09/README.ja.md) and [build instructions](distribution/image/README.ja.md).

The recorded component baseline compiled 499 canonical Ada files, ran 58 Ada test mains and 555 Python tests, and passed strict SPARK flow and level-4 proof for the units in each proof.gpr. These results apply to the source hashes in the evidence, not every later revision or the whole OS. The pinned container produces 18 byte-identical debug ELF binaries across two varied builds; all seven components also build and test independently. All 19 distribution DEBs match on rebuild. Evidence, hardware test limits and remaining Nia-specific integrations are listed in [STATUS.ja.md](STATUS.ja.md).

```sh
git clone --recurse-submodules https://github.com/minto-dane/niayan.git
cd niayan
make bootstrap       # Debian 13 development environment; installs dependencies
sh dev/run-limited.sh make check         # all native checks, bounded user scope
sh dev/run-limited.sh make private-dbus  # dedicated test bus; no desktop UI required
make toolchain       # checksum-pinned GNATprove download
sh dev/run-limited.sh make proof         # strict flow and proof; failures remain failures
```

For a fixed build environment and byte-for-byte binary comparisons, see [development instructions](dev/README.ja.md). For changes and generated files, see [CONTRIBUTING.md](CONTRIBUTING.md). For publishing the independent repositories, see [publishing instructions](dev/PUBLISHING.ja.md).

| Repository | Responsibility |
| --- | --- |
| assurance | Shared trust, authorization, evidence and verification tooling |
| pkgcore | Catalog/file changes, recovery and package semantics |
| statecore | Service/cluster state, health and recovery decisions |
| controlcore | Unified management contracts and internal controller |
| configcore | Configuration semantics, compatibility and generation |
| resolvercore | Candidate/proof verification independent of the proposal solver |
| capsulecore | Application generations, consent, permissions and broker contracts |
| distribution | Product specifications, layout and release gates |

The distribution targets Debian 13 Trixie with Nia as its sole package authority and without upstream source patches. This replacement remains under development; see the [current decision](distribution/docs/decisions/0002-native-package-authority.ja.md). The [earlier APT image recipe](distribution/image/README.ja.md) remains reproducible as a reference. Earlier Forky inputs and unconnected catalog/boot contracts must not be presented as accepted Trixie integrations. Historical evidence must not be cited as a current successful run.

Workspace-specific code is licensed under [BSD 3-Clause](LICENSE). Debian packages and vendored components retain their respective licenses.
