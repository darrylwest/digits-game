#!/usr/bin/env python3.11
# dpw@plaza.localdomain
# 2023-06-17 23:36:41

import tomllib

with open("games.toml", "rb") as f:
    print(f"{tomllib.load(f)}")

