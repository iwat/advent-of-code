import collections
import copy
import sys

grid = [list(l.strip()) for l in sys.stdin.readlines()]
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            start_x, start_y = x, y
        elif grid[y][x] == 'E':
            end_x, end_y = x, y


def find_path(grid, start, end):
    cost_map = {}

    q = collections.deque()
    q.append((start[0], start[1], 0))
    while len(q) > 0:
        x, y, c = q.pop()
        if (x, y) not in cost_map or cost_map[(x, y)] > c:
            cost_map[(x, y)] = c
        else:
            continue
        if (x, y) == end:
            continue

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dirs:
            next_x, next_y = x + d[0], y + d[1]
            if next_y < 0 or next_y > len(grid):
                continue
            if next_x < 0 or x > len(grid[next_y]):
                continue
            if grid[next_y][next_x] == '#':
                continue
            q.append((next_x, next_y, c + 1))

    return cost_map


print('-----')
cost_map = find_path(grid, (start_x, start_y), (end_x, end_y))
print(cost_map[(end_x, end_y)] - cost_map[(start_x, start_y)])

saving = {}
used = set()
path = list(cost_map.keys())
for i in range(len(path) - 1):
    for j in range(i + 1, len(path)):
        xy1 = path[i]
        xy2 = path[j]

        if (xy1, xy2) in used:
            continue
        used.add((xy1, xy2))
        used.add((xy2, xy1))

        distance = abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])
        if distance <= 20:
            save = abs(cost_map[xy1] - cost_map[xy2]) - distance
            #print(xy1, xy2, distance, save)
            if save not in saving:
                saving[save] = 0
            saving[save] += 1

print('=====')
good = 0
for k in sorted(saving.keys()):
    if len(grid) == 15 or k >= 100:
        #print(f'There are {saving[k]} cheats that save {k} picoseconds.')
        good += saving[k]
print(good)
