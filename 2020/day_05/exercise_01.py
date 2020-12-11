#! /usr/bin/env python3

import sys
    
def calculate_id(code):
    row = int(code[:7].replace('F','0').replace('B','1'),2)
    column = int(code[7:].replace('L','0').replace('R','1'),2)
    return row*8+column

f = open(sys.argv[1],'r')
max_id = 0
for line in f.readlines():
    max_id = max(max_id, calculate_id(line))
    
print('result: ', max_id)

