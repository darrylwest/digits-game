#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 23:16:43
#

set -eu

export HOST="${LOCAL_IP}:9890"
printf $HOST

curl -X 'POST' \
  "http://$HOST/problems" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "target": 271,
  "numbers": [2, 3, 7, 9, 11, 25]
}'
