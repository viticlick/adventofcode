#! /usr/bin/env  python3
import re, sys

counter = 0
with open(sys.argv[1], 'r') as f:
    for entry in re.split(r'(\r\n?|\n){2}', f.read(), flags=re.MULTILINE):
        keys = set(re.findall(r'([a-z])', entry))
        print(keys)
        print('-------')
        counter = counter + len(keys)

print('number of responses: ', counter)