# SPDX-License-Identifier: BSD-3-Clause
SHELL := /bin/sh
REPOS := assurance pkgcore statecore controlcore configcore resolvercore capsulecore
GNATPROVE ?= $(HOME)/.cache/niaos/toolchains/gnatprove-x86_64-linux-16.1.0-1/bin/gnatprove
.PHONY: help bootstrap toolchain build check source-check native-check proof generated rebind private-dbus license-check
help:
	@echo 'bootstrap    Install Debian 13 development dependencies in this Distrobox'
	@echo 'toolchain    Download and verify the pinned GNATprove archive'
	@echo 'build        Compile every unit and link all 18 application mains'
	@echo 'check        Source checks, all-unit builds, CLI links and all Ada tests'
	@echo 'private-dbus Run native protocol tests on a dedicated private bus'
	@echo 'proof        Run strict SPARK flow and level-4 proof (no download)'
	@echo 'generated    Check generated independent component CI/test runners'
	@echo 'image-check  Check Debian image preparation tools without building an ISO'
bootstrap:
	sudo sh dev/setup-debian.sh
toolchain:
	python3 assurance/ci/install-gnatprove.py
build:
	@set -eu; for repo in $(REPOS); do $(MAKE) -C "$$repo" compile-all build; done
check native-check: license-check
	python3 assurance/ci/run-engineering-checks.py --mode build --include-host-observers
source-check: license-check
	python3 assurance/ci/run-engineering-checks.py --mode source
private-dbus:
	sh capsulecore/ci/test-consent.sh
license-check:
	python3 dev/check-licenses.py
proof:
	@test -x "$(GNATPROVE)" || { echo 'Run make toolchain first, or specify GNATPROVE=/absolute/path/gnatprove' >&2; exit 78; }
	PATH="$(dir $(GNATPROVE)):$$PATH" python3 assurance/ci/run-engineering-checks.py --mode proof --timeout 7200
generated:
	python3 assurance/ci/sync-component-ci.py
rebind:
	python3 assurance/ci/rebind-development.py --write --acknowledge-incompatible-change --public-test-only
	python3 assurance/ci/sync-component-ci.py --write

.PHONY: reproducible
reproducible:
	python3 dev/reproducible-build.py

.PHONY: image-check
image-check:
	$(MAKE) -C distribution image-check
