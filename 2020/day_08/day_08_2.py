#! /usr/bin/env  python3
import re, copy

ops = []
f = open('input','r')
for line in f.readlines():
    op, v = re.findall(r'(\w+) ([+-]\d+)', line)[0]
    ops.append((op, v, 0))

def calculate(operations):
    acc = 0
    index = 0
    while True:
        op, v, x = operations[index]
        operations[index] = (op, v, 1)
        if x == 1 :
            raise Exception("repeated operations")
        if op == 'nop':
            index = index + 1
        elif op == 'acc':
            acc = acc + int(v)
            index = index + 1
        elif op == 'jmp':
            index = index + int(v)
        if index == len(operations):
            return acc

for index in range(len(ops)):
    cp = copy.deepcopy(ops)
    op,v,x = cp[index]
    if op == 'nop':
        cp[index] = ('jmp', v, 0)
    elif op == 'jmp':
        cp[index] = ('nop', v, 0)
    try:
        acc = calculate(cp)
        print('result: ', acc)
        break
    except:
        continue

