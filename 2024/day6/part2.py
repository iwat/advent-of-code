import copy
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

initial_x, initial_y, initial_direction = find_initial(grid)

def run(x, y, direction, grid):
    grid = copy.deepcopy(grid)
    stat = [[set() for _ in range(len(row))] for row in grid]
    is_loop = False
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

        if grid[next_y][next_x] in ['#', 'O']:
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
            if direction in stat[y][x]:
                is_loop = True
                break
            else:
                stat[y][x].add(direction)

            x, y = next_x, next_y
            grid[y][x] = direction

        #print('\n'.join([''.join(row) for row in grid]))
        #print()
        #time.sleep(0.05)
    return grid, is_loop

marked_grid, _ = run(initial_x, initial_y, initial_direction, grid)
#print('\n'.join([''.join(row) for row in marked_grid]))

loops = 0
for x in range(width):
    for y in range(height):
        if not (x == initial_x and y == initial_y) and marked_grid[y][x] == 'X':
            fixed_grid = copy.deepcopy(grid)
            fixed_grid[y][x] = 'O'
            marked_fixed_grid, is_loop = run(initial_x, initial_y, initial_direction, fixed_grid)
            if is_loop:
                loops += 1
                #print(f'Loop ({x},{y})')
                #print('\n'.join([''.join(row) for row in marked_fixed_grid]))

print(loops)
