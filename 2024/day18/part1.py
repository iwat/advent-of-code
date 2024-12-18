import collections
import sys
import time

size = int(sys.argv[1])
max_corruption = int(sys.argv[2])
grid = [['.' for _ in range(size)] for _ in range(size)]

seq = [tuple([int(xy) for xy in l.strip().split(',')]) for l in sys.stdin.readlines()]
corruption = set()
for e in seq:
    if len(corruption) >= max_corruption:
        break
    corruption.add(e)
    grid[e[1]][e[0]] = '#'

print('-----')
print('\n'.join([''.join(row) for row in grid]))

cost_grid = {}

q = collections.deque()
q.append((0, 0, 0))
while len(q) > 0:
    x, y, cost = q.popleft()
    if (x, y) in cost_grid and cost_grid[(x, y)] <= cost:
        continue

    cost_grid[(x, y)] = cost

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for m in moves:
        new_x, new_y = x + m[0], y + m[1]
        if new_x >= 0 and new_x < size and new_y >= 0 and new_y < size:
            if grid[new_y][new_x] == '.':
                q.append((new_x, new_y, cost + 1))

print('=====')
q = collections.deque()
q.append((size - 1, size - 1, cost_grid[(size - 1, size - 1)]))
while len(q) > 0:
    x, y, cost = q.popleft()
    grid[y][x] = 'O'
    if cost == 0:
        break

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for m in moves:
        new_x, new_y = x + m[0], y + m[1]
        if (new_x, new_y) in cost_grid and cost_grid[(new_x, new_y)] < cost:
            q.append((new_x, new_y, cost_grid[(new_x, new_y)]))
            break

print('\n'.join([''.join(row) for row in grid]))

print('=====')
print(cost_grid[(size - 1, size - 1)])

