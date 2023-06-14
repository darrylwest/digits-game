#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 15:55:45
#

set -eu

HOST=$LOCAL_IP
# HOST=127.0.0.1

# --workers 4 # this is ignored when --reload is used

uvicorn --port 9890 --host $HOST --app-dir server main:app --reload 

