#! /usr/bin/env  python3
import re, sys

def contained(color, colorset):
    if colorset.get(color) is None:
        print('empty set for color ', color)
        return {color}
    else:
        containers = set()
        containers.add(color)
        for c in colorset[color]:
            colors = contained(c, colorset)
            containers = containers | colors
        print(color, ' contained in ', containers)
        return containers


counter = 0
with open('input', 'r') as f:

    colorset = dict()
    for line in f.readlines():
        base_color = re.findall(r'(\w+ \w+) bags contain', line)[0]
        colors = re.findall(r'\d+ (\w+ \w+)',line)
        for color in colors:
            containers = colorset.get(color, set())
            containers.add(base_color) 
            colorset[color] = containers

    #print(colorset)
    colors = contained('shiny gold', colorset)
    print(colors)
    print(len(colors) - 1)
    

