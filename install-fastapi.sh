#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 15:43:23
#

set -eu

python3 -m pip install fastapi
python3 -m pip install "uvicorn[standard]"

exit $?

