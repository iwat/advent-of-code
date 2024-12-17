import collections
import math
import time
import sys

grid = [list(l.strip()) for l in sys.stdin.readlines()]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            initial_x = x
            initial_y = y
            grid[y][x] = '.'
        elif grid[y][x] == 'E':
            target_x = x
            target_y = y
            grid[y][x] = '.'

def print_grid(grid):
    print('\n'.join([''.join(row) for row in grid]))

print_grid(grid)

visited = {}
q = collections.deque([(initial_x, initial_y, '>', 0)])

while len(q) > 0:
    x, y, direction, score = q.popleft()
    if (x, y, direction) in visited and visited[(x, y, direction)] < score:
        continue

    visited[(x, y, direction)] = score
    if (x, y) == (target_x, target_y):
        continue

    if grid[y][x + 1] == '.':
        if direction == '>':
            q.append((x + 1, y, '>', score + 1))
        elif direction == '<':
            q.append((x, y, '>', score + 2000))
        else:
            q.append((x, y, '>', score + 1000))
    if grid[y][x - 1] == '.':
        if direction == '<':
            q.append((x - 1, y, '<', score + 1))
        elif direction == '>':
            q.append((x, y, '<', score + 2000))
        else:
            q.append((x, y, '<', score + 1000))
    if grid[y + 1][x] == '.':
        if direction == 'v':
            q.append((x, y + 1, 'v', score + 1))
        elif direction == '^':
            q.append((x, y, 'v', score + 2000))
        else:
            q.append((x, y, 'v', score + 1000))
    if grid[y - 1][x] == '.':
        if direction == '^':
            q.append((x, y - 1, '^', score + 1))
        elif direction == 'v':
            q.append((x, y, '^', score + 2000))
        else:
            q.append((x, y, '^', score + 1000))


best_end = []
best_score = math.inf
for d in ['>', 'v', '<', '^']:
    if (target_x, target_y, d) in visited:
        if visited[(target_x, target_y, d)] < best_score:
            best_score = visited[(target_x, target_y, d)]
            best_end = [([(target_x, target_y, d)], best_score)]
        elif visited[(target_x, target_y, d)] == best_score:
            best_end.append(([(target_x, target_y, d)], best_score))

print('-----')
for end in best_end:
    print(end)
