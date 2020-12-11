#! /usr/bin/env  python3
import re

ops = []
f = open('input','r')
for line in f.readlines():
    op, v = re.findall(r'(\w+) ([+-]\d+)', line)[0]
    ops.append((op, v, 0))

acc = 0
index = 0
while True:
    op, v, x = ops[index]
    ops[index] = (op, v, 1)
    if x == 1 :
        break
    if op == 'nop':
        index = index + 1
    elif op == 'acc':
        acc = acc + int(v)
        index = index + 1
    elif op == 'jmp':
        index = index + int(v)

print('acc has the value: ', acc)

