import copy
import sys


def stuck_on(grid):
    grid[0][0] = '#'
    grid[0][-1] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'

grid = [list(l.strip()) for l in sys.stdin.readlines()]
stuck_on(grid)

print('-----')
print('\n'.join([''.join(row) for row in grid]))

steps = 100
if len(grid) == 6:
    steps = 5


for i in range(steps):
    new_grid = copy.deepcopy(grid)
    print('-----', i + 1)
    for y in range(len(new_grid)):
        for x in range(len(new_grid[y])):
            neighbor_deltas = [
                    (-1, -1), (0, -1), (1, -1),
                    (-1,  0),          (1,  0),
                    (-1,  1), (0,  1), (1,  1),
                    ]
            neighbor_on = 0
            for delta in neighbor_deltas:
                new_x, new_y = x + delta[0], y + delta[1]
                if new_y < 0 or new_y >= len(grid):
                    continue
                if new_x < 0 or new_x >= len(grid[y]):
                    continue
                if grid[new_y][new_x] == '#':
                    neighbor_on += 1

            if grid[y][x] == '#':
                if neighbor_on == 2 or neighbor_on == 3:
                    new_grid[y][x] = '#'
                else:
                    new_grid[y][x] = '.'
            else: # == '.'
                if neighbor_on == 3:
                    new_grid[y][x] = '#'
                else:
                    new_grid[y][x] = '.'
    stuck_on(new_grid)
    print('\n'.join([''.join(row) for row in new_grid]))
    grid = new_grid

print('=====')
print(sum([col == '#' for row in grid for col in row]))
