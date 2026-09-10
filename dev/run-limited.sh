#!/bin/sh
# SPDX-License-Identifier: BSD-3-Clause
# Local development: a transient user scope, removed after its processes exit.
# Failure to create the scope is a failure; never retry without the limits.
set -eu
[ "$(id -u)" -ne 0 ] || { echo 'Run the development scope as your ordinary user' >&2; exit 78; }
[ "$#" -gt 0 ] || { echo 'Usage: dev/run-limited.sh command [argument ...]' >&2; exit 64; }
limit_tools=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec systemd-run --user --scope --collect \
  -p MemoryMax=3G -p MemorySwapMax=0 -p CPUQuota=100% -p TasksMax=128 \
  -- python3 "$limit_tools/limited-exec.py" "$@"
