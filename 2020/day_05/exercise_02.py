#! /usr/bin/env python3

import sys
    
def calculate_id(code):
    row = int(code[:7].replace('F','0').replace('B','1'),2)
    column = int(code[7:].replace('L','0').replace('R','1'),2)
    return row*8+column

f = open(sys.argv[1],'r')
lst = [None] * 128 * 8
for line in f.readlines():
    lst[calculate_id(line)] = 'x'

for i in range(1,128*8):
    if lst[i] is None and lst[i-1] is not None and lst[i+1] is not None:
        print('your seat is: ', i)
    

