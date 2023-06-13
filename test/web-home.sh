#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 16:10:22
#

set -eu

HOST="$LOCAL_IP:9890/"

curl -X 'GET' "http://$HOST" 


