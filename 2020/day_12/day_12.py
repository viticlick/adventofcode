#! /usr/bin/env  python3

import re

class Ship():

    def __init__(self):
        self.compass = ['N','E','S','W']
        self.facing_to = 1
        self.position = {
            "N" : 0,
            "S" : 0,
            "E" : 0,
            "W" : 0
        }
    
    def move(self, action, value):
        if action in self.position:
            self.position[action] += value
        elif action == 'F':
            self.position[self.compass[self.facing_to]] += value
        elif action == 'R':
            self.facing_to = int((self.facing_to + value/90) % 4)
        elif action == 'L':
            self.facing_to = int((self.facing_to - value/90) % 4)

    def manhattan(self):
        return abs(self.position['E'] - self.position['W']) + abs(self.position['N'] - self.position['S'])

ship = Ship()

f = open('input', 'r')
actions = [ re.findall(r'([NSEWLRF])(\d+)', line)[0] for line in f.readlines()]
[ship.move(action, int(value)) for action, value in actions]

print('distance: ',ship.manhattan())

