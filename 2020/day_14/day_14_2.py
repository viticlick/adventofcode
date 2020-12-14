#! /usr/bin/env  python3

import re

MASK_REGEX = r'mask = ([X01]+)'
MEMORY_REGEX = r'mem\[(\d+)\] = (\d+)'

number_of_X = 0
ones_mask = 0
mask = ''
mem = {}
f = open('input', 'r')
for line in f.readlines():
    if re.match(MASK_REGEX, line):
        mask = re.findall(MASK_REGEX, line)[0]
        number_of_X = mask.count('X')
        ones_mask = int(mask.replace('X','0'), 2)

    else:
        position, value =  re.findall(MEMORY_REGEX, line)[0]
        bin_position = str(bin(int(position) | ones_mask))[2:]

        for n in range(2**number_of_X):
            X_replacements = ['0'] * (number_of_X - len(str(bin(n))[2:])) + list(str(bin(n))[2:])
            dir_value = (['0'] * (36 - len(bin_position))) + list(bin_position)
            mask_copy = mask[:]
            for v in X_replacements:
                X_index = mask_copy.index('X')
                dir_value[X_index] = v
                mask_copy = mask_copy.replace('X','0',1)
            mem[''.join(dir_value)] = int(value)

acc = 0            
for value in mem.values():
    acc = acc + value
print('value: ', acc)


            
acc = 0
for value in mem.values():
    acc = acc + value
print(acc)



    