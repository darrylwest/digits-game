#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 16:09:40
#

set -eu

HOST='127.0.0.1:9890'

curl -X 'GET' "http://$HOST/items/56893?q=1%2C2%2C3%2C4%2C5%2C6" -H 'accept: application/json'


