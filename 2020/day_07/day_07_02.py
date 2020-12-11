#! /usr/bin/env  python3
import re, sys

def bags(colorset, color):
    if colorset.get(color) == []:
        print(color, ' has no bags inside')
        return 1

    print(color, ' contains:')
    counter = 0
    for n, c in colorset[color]:
        counter = counter + int(n) * bags(colorset,c)
        print(n, ' of ', c, ' bags')

    return counter + 1

counter = 0
with open('input', 'r') as f:

    colorset = dict()
    for line in f.readlines():
        base_color = re.findall(r'(\w+ \w+) bags contain', line)[0]
        colors = re.findall(r'(\d+) (\w+ \w+)',line)
        colorset[base_color] = colors
    
    print(colorset)
    print(bags(colorset, 'shiny gold') - 1)

    

