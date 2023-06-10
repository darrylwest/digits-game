#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-10 23:02:17
#

set -eu

watchexec -w digits.py -d 500 -c ./digits.py

exit $?

