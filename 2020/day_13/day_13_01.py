#! /usr/bin/env  python3

f = open('input', 'r')
f.readline()
values =  f.readline().split(',')
values_with_offset = [ (int(t) , idx) for idx, t in enumerate(values) if t != 'x']

timestamp = 0
step = int(values[0])
buses = len(values_with_offset)
while True:
    print('checking timestamp: ', timestamp)
    matches = 0
    for value, offset in values_with_offset:
        if (timestamp + offset) % value != 0:
            break
        matches = matches + 1
    if matches == buses:
        _, offset = values_with_offset[:1][0]
        print('the value is: ', timestamp + offset)
        break
    timestamp = timestamp + step
    