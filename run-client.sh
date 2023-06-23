#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 17:59:14
#

set -eu

# should replace this with caddy proxy with certs to prepare for production

python3 -m http.server --bind 0.0.0.0 -d web/ 9800

