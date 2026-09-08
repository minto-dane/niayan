# Nia OS components

Nia OS is a Linux distribution under development. This workspace pins seven independent Ada/SPARK component repositories and the distribution specification repository as Git submodules. [日本語](README.ja.md).

**Development sources; not production qualified.** Native builds and tests are being validated; formal proof and the external integrations listed in [STATUS.ja.md](STATUS.ja.md) are separate acceptance gates. This repository does not produce a bootable OS yet.

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

The target policy remains authenticated Debian 14 Forky DEB inputs, an authoritative Nia installed-state catalog, XFS persistent storage and a FAT32 ESP. Debian 13 is the development host. Historical imported evidence is retained and must not be cited as a current successful run.

Licensed under [MIT](LICENSE); component repositories retain their license notices.
