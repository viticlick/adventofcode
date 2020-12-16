#! /usr/bin/env  python3

import re

def parse_field_group(line):
    values = re.findall(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
    name, low_1, high_1 , low_2, high_2 = values
    return (name, (int(low_1), int(high_1)), (int(low_2), int(high_2)))

def parse_ticket(line):
    return [int(x) for x in re.findall(r'(\d+)', line)]

def is_in_validator(field, validation):
    _ , v1, v2 = validation
    low_1, high_1 = v1
    low_2, high_2 = v2
    return low_1 <= field <= high_1 or low_2 <= field <= high_2

def create_validator(validators, my_ticket):
    result = []
    for value in my_ticket:
        ops = set()
        for id_v, validation in enumerate(validators):
            if is_in_validator(value, validation):
                ops.add(id_v)
        result.append(ops)
    return result

f = open('input', 'r')
validators = []
while True:
    line = f.readline()
    if line == '\n':
        break
    validators.append(parse_field_group(line))


f.readline()
my_ticket = parse_ticket(f.readline())
ticket_field_sets = create_validator(validators, my_ticket)

for line in f.readlines():
    values = parse_ticket(line)
    ticket_sets = []
    is_invalid = False
    for id_value, field in enumerate(values):
        ops = set()
        for index in ticket_field_sets[id_value]:
            if is_in_validator(field, validators[index]):
                ops.add(index)
        if len(ops) is 0:
            is_invalid = True
            break
        ticket_sets.append(ops)

    if is_invalid or len(ticket_sets) == 0:
        continue
    
    ticket_field_sets = [ a & b for a, b in zip(ticket_field_sets, ticket_sets)]
    

sorted_set = ticket_field_sets[:]
sorted_set.sort(key=lambda x:len(x))

for line in sorted_set:
    for idx, x in enumerate(ticket_field_sets):
        if len(x) > 1:
            y = x.difference(line)
            ticket_field_sets[idx] = y

acc = 1
counter = 0
for id_value, s in enumerate(ticket_field_sets):
    id_validator = s.pop()
    name, _, _ = validators[id_validator]
    if name.startswith('departure'):
        acc = acc * my_ticket[id_value]

print(acc)