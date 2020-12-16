#! /usr/bin/env  python3

import re

validator = []

f = open('input', 'r')
while True:
    line = f.readline()
    if line == '\n':
        break
    ranges = re.findall(r'(\d+)-(\d+)', line)
    for r in ranges:
        low, high = r
        validator.append((int(low), int(high)))

for _ in range(0,4):
    f.readline()

acc = 0
for line in f.readlines():
    fields = re.findall(r'(\d+)', line)
    for field in fields:
        matched = False
        field_int = int(field)
        for validation in validator:
            low, high = validation
            matched = low <= field_int <= high
            if matched:
                break
        if not matched:
            acc = acc + field_int


print(acc)