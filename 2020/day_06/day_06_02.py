#! /usr/bin/env  python3
import re, sys
from functools import reduce


counter = 0
with open(sys.argv[1], 'r') as f:
    groups = []
    group = []
    for line in f.readlines():
        if line == '\n':
            groups.append(group)
            group = []
        else:
            group.append(set(re.findall(r'([a-z])', line)))

    groups.append(group)

    for responses in groups:
        print()
        count = len(reduce((lambda x, y: x & y), responses))
        print(count)
        print('---------')
        counter = counter + count
    print('number of responses: ', counter)
