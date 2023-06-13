#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 23:16:43
#

set -eu

HOST='127.0.0.1:9890'

curl -X 'POST' \
  "http://$HOST/problems" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "target": 414,
  "numbers": [1, 2, 3, 4, 20, 25]
}'

