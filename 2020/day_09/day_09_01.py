#! /usr/bin/env  python3
import itertools, sys

preamble = 25
weakness = None
f = open('input', 'r')

values = [int(line) for line in f.readlines()]
for index in range(preamble, len(values)):
    permutations = list(itertools.permutations(values[index-preamble:index],r=2))
    sums = set([x + y for x, y in permutations])
    if not values[index] in sums :
        weakness = values[index]
        break

print('the value is: ', values[index])
for x in range(len(values)):
    acc = 0
    for y in range(x,len(values)):
        acc = acc + values[y]
        if acc == weakness:
            smallest = min(values[x:y])
            largest = max(values[x:y])
            print(smallest,  largest, smallest + largest )
            sys.exit()
        if acc > weakness:
            break
