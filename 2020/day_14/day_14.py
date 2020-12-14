#! /usr/bin/env  python3

import re

MASK_REGEX = r'mask = ([X01]+)'
MEMORY_REGEX = r'mem\[(\d+)\] = (\d+)'

ones_mask = 0
zeros_mask = 0
mem = {}
f = open('input', 'r')
for line in f.readlines():
    if re.match(MASK_REGEX, line):
        mask = re.findall(MASK_REGEX, line)[0]
        ones_mask = int(mask.replace('X','0'), 2)
        zeros_mask = int(mask.replace('X','1'), 2)
    
    else:
        position, value =  re.findall(MEMORY_REGEX, line)[0]
        mem[position] = (int(value) | ones_mask) & zeros_mask 

acc = 0
for value in mem.values():
    acc = acc + value
print(acc)



    