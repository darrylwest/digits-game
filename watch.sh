#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-10 23:02:17
#

set -eu

target=digits.py
target=short.py

watchexec -w $target -d 500 -c ./$target

exit $?

