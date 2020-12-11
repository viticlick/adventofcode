#! /usr/bin/env  python3

def neighbours(seats, x, y):
    rows = len(seats)
    columns = len(seats[0])
    highest = max(rows,columns)
    neighbours = 0
    for ix in range(1,x+1):
        if seats[x - ix][y] == 'L':
            break
        if seats[x - ix][y] == '#':
            neighbours = neighbours + 1
            break
    for ix in range(x+1,rows):
        if seats[ix][y] == 'L':
            break
        if seats[ix][y] == '#':
            neighbours = neighbours + 1
            break
    for iy in range(1,y+1):
        if seats[x][y - iy] == 'L':
            break
        if seats[x][y - iy] == '#':
            neighbours = neighbours + 1
            break
    for iy in range(y+1,columns):
        if seats[x][iy] == 'L':
            break
        if seats[x][iy] == '#':
            neighbours = neighbours + 1
            break
    for n in range(1,highest):
        if x + n >= rows or y + n >= columns:
            break
        if seats[x+n][y + n] == 'L':
            break
        if seats[x+n][y + n] == '#':
            neighbours = neighbours + 1
            break
    for n in range(1,highest):
        if x + n >= rows or y - n < 0:
            break
        if seats[x + n][y - n] == 'L':
            break
        if seats[x + n][y - n] == '#':
            neighbours = neighbours + 1
            break
    for n in range(1,highest):
        if x - n < 0 or y - n < 0:
            break
        if seats[x - n][y - n] == 'L':
            break
        if seats[x - n][y - n] == '#':
            neighbours = neighbours + 1
            break
    for n in range(1,highest):
        if x - n < 0 or y + n >= columns:
            break
        if seats[x - n][y + n] == 'L':
            break
        if seats[x - n][y + n] == '#':
            neighbours = neighbours + 1
            break
    return neighbours

def new_state(seats, x, y):
    occupied = neighbours(seats, x, y)
    if seats[x][y] == 'L' and occupied == 0:
        return '#'
    if seats[x][y] == '#' and occupied >= 5:
        return 'L'
    return seats[x][y]

f = open('input', 'r')
seats = [list(line.strip()) for line in f.readlines()]
while True:
    next_generation = []
    for x in range(len(seats)):
        next_generation.append([])
        for y in range(len(seats[0])):
            next_generation[x].append(new_state(seats, x, y))
    if seats == next_generation:
        seats_occupied = 0
        for x in range(len(seats)):
            for y in range(len(seats[0])):
                if seats[x][y] == '#':
                    seats_occupied = seats_occupied + 1
        print(seats_occupied)
        break

    seats = next_generation