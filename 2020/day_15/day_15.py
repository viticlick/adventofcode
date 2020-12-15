#! /usr/bin/env  python3

import re

INPUT = '0,3,1,6,7,5'
TOTAL = 30000000

vector = [None] * TOTAL
index = 1
value = 0
for x in re.findall(r'(\d+)', INPUT):
    vector[int(x)] = (index, index)
    index = index + 1
    value =  int(x)
 
for position in range(index, TOTAL + 1):
    
    low, high = vector[value]
    value = high - low

    if vector[value] is None:
        vector[value] = (position, position)
    else:
        low, high = vector[value]
        vector[value] = (high, position)

print(value)