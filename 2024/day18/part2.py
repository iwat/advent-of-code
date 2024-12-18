import collections
import sys
import time

size = int(sys.argv[1])
seq = [tuple([int(xy) for xy in l.strip().split(',')]) for l in sys.stdin.readlines()]

def solve(max_corruption):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    corruption = set()
    last_coor = None
    for e in seq:
        if len(corruption) >= max_corruption:
            break
        corruption.add(e)
        grid[e[1]][e[0]] = '#'
        last_coor = (e[0], e[1])

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

    if (size - 1, size - 1) in cost_grid:
        return (last_coor, cost_grid[(size - 1, size - 1)])
    return (last_coor, None)

left = 0
right = size*size
while left <= right:
    m = (right + left) // 2
    coor, sol = solve(m)
    if sol:
        print(m, 'POSSIBLE', sol, coor)
        left = m + 1
    else:
        print(m, 'BLOCKED', coor)
        right = m - 1
print(m - 1, solve(m - 1))
print(m, solve(m))
print(m + 1, solve(m + 1))
