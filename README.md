# Nia OS components

Nia OS is a Linux distribution under development. This workspace pins seven independent Ada/SPARK component repositories and the distribution specification repository as Git submodules. [日本語](README.ja.md).

**Bootable, installable Debian 13 KDE development image; not production qualified.** The actual ISO passed BIOS, UEFI, Secure Boot, Japanese input, offline/online installation and reboot, and signed APT metadata retrieval in bounded VMs. Two independent ISO builds match byte for byte, and the corresponding source archives have been collected and verified after copying. See the [distribution acceptance](distribution/evidence/debian13/accepted-09/README.ja.md) and [build instructions](distribution/image/README.ja.md).

All 499 canonical Ada files compile, all 58 Ada test mains and 555 Python tests pass across their required contexts, and all seven components pass strict SPARK flow and full level-4 proof for the units in each proof.gpr. The pinned container produces 18 byte-identical debug ELF binaries across two varied builds; all seven components also build and test independently. All 19 distribution DEBs match on rebuild. Evidence, hardware test limits and remaining Nia-specific integrations are listed in [STATUS.ja.md](STATUS.ja.md).

```sh
git clone --recurse-submodules <workspace-url>
cd <workspace>
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
| controlcore | Unified management and the `nia` CLI |
| configcore | Configuration semantics, compatibility and generation |
| resolvercore | Candidate/proof verification independent of the proposal solver |
| capsulecore | Application generations, consent, permissions and broker contracts |
| distribution | Product specifications, layout and release gates |

The distribution now targets Debian 13 Trixie, retaining upstream packages and APT/dpkg, live-build and Debian Installer. NiaOS additions are separate DEBs; component sources are not patched to make the image boot. See the [image build instructions](distribution/image/README.ja.md) and [decision](distribution/docs/decisions/0001-debian13.ja.md). The earlier Forky/catalog profiles and contracts remain a research model, not the deployed image's package authority. Historical evidence must not be cited as a current successful run.

Workspace-specific code is licensed under [MIT](LICENSE). Debian packages and vendored components retain their respective licenses.
