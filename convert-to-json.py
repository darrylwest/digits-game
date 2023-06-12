#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-12 14:37:26

import csv
import json
from ast import literal_eval

csvfile = open('games.log', 'r')
jsonfile = open('games.json', 'w')

fieldnames = ("target","numbers","result")
reader = csv.DictReader(csvfile, fieldnames)

data = []
for row in reader:
    row['target'] = int(row['target'])
    row['numbers'] = literal_eval(row['numbers'])
    data.append(row)

out = json.dumps(data, indent=2)
jsonfile.write(out)

