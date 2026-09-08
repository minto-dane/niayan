#!/bin/sh
# SPDX-License-Identifier: MIT
# Install development tools into the existing Debian Distrobox; not the target OS.
set -eu
[ "$(id -u)" -eq 0 ] || { echo 'Run this dependency installer with sudo' >&2; exit 78; }
. /etc/os-release
[ "$ID" = debian ] && [ "$VERSION_ID" = 13 ] || { echo 'Use the pinned Debian 13 development container' >&2; exit 78; }
base=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
apt-get update
xargs -r apt-get install -y --no-install-recommends < "$base/packages.txt"
