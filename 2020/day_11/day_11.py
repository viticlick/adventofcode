#! /usr/bin/env  python3

def neighbours(seats, x, y):
    rows = len(seats)
    columns = len(seats[0])
    neighbours = 0
    for ix in range(x - 1, x + 2):
        if not -1 < ix < rows:
            continue
        for iy in range(y - 1, y + 2):
            if not -1 < iy < columns:
                continue
            if ix == x and iy == y:
                continue 
            neighbours = (neighbours + 1) if seats[ix][iy] == '#' else neighbours
    return neighbours

def new_state(seats, x, y):
    occupied = neighbours(seats, x, y)
    if seats[x][y] == 'L' and occupied == 0:
        return '#'
    if seats[x][y] == '#' and occupied >= 4:
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
    # print('generation')
    # for row in next_generation:
    #     print(row)

