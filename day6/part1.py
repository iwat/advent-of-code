import sys
import time


def find_initial(grid):
    for x in range(width):
        for y in range(height):
            if grid[y][x] == '^':
                return (x, y, '^')


grid = [list(l.strip()) for l in sys.stdin.readlines() if l.strip() != '']
width = len(grid[0])
height = len(grid)

x, y, direction = find_initial(grid)

while True:
    if direction == '^':
        next_x, next_y = x, y-1
    elif direction == '>':
        next_x, next_y = x+1, y
    elif direction == 'V':
        next_x, next_y = x, y+1
    elif direction == '<':
        next_x, next_y = x-1, y

    if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height:
        if grid[y][x] != 'X':
            grid[y][x] = 'X'
        break

    if grid[next_y][next_x] == '#':
        if direction == '^':
            direction = '>'
        elif direction == '>':
            direction = 'V'
        elif direction == 'V':
            direction = '<'
        elif direction == '<':
            direction = '^'
        continue
    else:
        grid[y][x] = 'X'
        x, y = next_x, next_y
        grid[y][x] = direction

    #print('\n'.join([''.join(row) for row in grid]))
    #print()

#print('\n'.join([''.join(row) for row in grid]))
#print()
print(len([c for row in grid for c in row if c == 'X']))
