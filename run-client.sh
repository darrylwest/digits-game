#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 17:59:14
#

set -eu

cd web

python3 -m http.server 3000

