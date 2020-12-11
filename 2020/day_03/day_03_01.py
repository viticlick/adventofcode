import sys

def calculate_relative_position(position, row_length, right_movements):
    return (position + right_movements) % row_length

def read_rows(path):
    f = open(path, 'r')
    return [line.strip() for line in f.readlines()] 
    

if __name__ == '__main__':
    path = sys.argv[1]
    right_movements = int(sys.argv[2])
    down_movements = int(sys.argv[3])
    trees = 0
    position = right_movements * -1
    rows = read_rows(path)
    row_length = len(rows[0])
    row_count = 1
    for row in rows:
        row_count = row_count + 1
        if row_count % down_movements != 0:
            continue
        position = calculate_relative_position(position, row_length, right_movements)
        char_replacement = '0'
        if row[position] == '#' :
            trees = trees + 1
            char_replacement = 'X'

        row = row[:position] + char_replacement + row[position+1:]
        print(row)
    print('total of trees: ', trees)

