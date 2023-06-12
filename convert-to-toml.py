#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-12 14:53:12

import toml
import json

with open('games.json', 'r') as jsonfile:
    data = json.load(jsonfile)

data = {'game': data}
toml_str = toml.dumps(data)

with open('games.toml', 'w') as tomlfile:
    tomlfile.write(toml_str)

