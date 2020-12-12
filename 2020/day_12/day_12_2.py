#! /usr/bin/env  python3

import re

class Ship():

    def __init__(self):
        self.compass = {
            'N': 0,
            'E': 1,
            'S': 2,
            'W': 3
        }
        self.position = [0,0,0,0]
        self.waypoint = [1,10,0,0]
    
    def move(self, action, value):
        if action in self.compass:
            self.waypoint[self.compass[action]] += value
        elif action == 'R':
            shift = int(value/90)
            self.waypoint = self.waypoint[-shift:] + self.waypoint[:-shift]
        elif action == 'L':
            shift = int(value/90)
            self.waypoint = self.waypoint[shift:] + self.waypoint[:shift]
        elif action == 'F':
            self.position = [x + y * value for x, y in zip(self.position, self.waypoint)]

    def manhattan(self):
        return abs(self.position[1] - self.position[3]) + abs(self.position[0] - self.position[2])

ship = Ship()

f = open('test', 'r')
actions = [ re.findall(r'([NSEWLRF])(\d+)', line)[0] for line in f.readlines()]
for action, value in actions:
    ship.move(action, int(value))

print('distance: ',ship.manhattan())

