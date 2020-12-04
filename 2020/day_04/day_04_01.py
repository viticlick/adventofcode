#! /usr/bin/env  python3
import re, sys

counter = 0
with open(sys.argv[1], 'r') as f:
    for entry in re.split(r'(\r\n?|\n){2}', f.read(), flags=re.MULTILINE):
        keys = set(re.findall(r'\b(byr|iyr|eyr|hgt|hcl|ecl|pid):', entry))
        if len(keys) >= 7:
            counter = counter + 1

print('number of valid entries: ', counter)
