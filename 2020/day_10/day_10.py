#! /usr/bin/env  python3
f = open('input', 'r')
values = [int(line) for line in f.readlines()]
values.sort()
previous, diff_of_one, diff_of_three = 0, 0, 1
for current in values:
    if current - previous == 1:
        diff_of_one = diff_of_one + 1
    if current - previous == 3:
        diff_of_three = diff_of_three + 1
    previous = current

print('result part 1: ', diff_of_one * diff_of_three)

max_value = previous + 3
series = [0] + values[:] + [max_value]
memoized_values = [None for i in range(len(series))]
def adapters(values, index, prev):

    if index >= len(values):
        return 0

    if values[index] - prev > 3 :
        memoized_values[index] = 0
        return 0

    if memoized_values[index] is not None:
        return memoized_values[index]

    if values[index] == max_value:
        memoized_values[index] = 1
        return 1
    
    acc = 0
    for i in range(1,4):
        acc = acc + adapters(values, index + i, values[index])
    
    memoized_values[index] = acc
    return acc

print('result part 2: ', adapters(series, 0, 0))