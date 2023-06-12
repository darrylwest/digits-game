#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-12 14:37:26

import csv
import json

csvfile = open('games.csv', 'r')
jsonfile = open('games.json', 'w')

fieldnames = ("target","numbers","result")
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([row for row in reader])
jsonfile.write(out)

