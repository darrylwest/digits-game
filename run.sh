#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-06-13 15:55:45
#

set -eu

# cd web 
#
HOST=$LOCAL_IP

uvicorn --port 9890 --host $HOST --app-dir web main:app --reload

