import functools
import re
import sys

WIDTH = 101
HEIGHT = 103
MIDX = WIDTH >> 1
MIDY = HEIGHT >> 1


def printgrid(robots):
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for r in robots:
        if grid[r['py']][r['px']] == '.':
            grid[r['py']][r['px']] = 1
        else:
            grid[r['py']][r['px']] += 1

    print('\n'.join([''.join([str(x) for x in grid[y]]) for y in range(HEIGHT)]))


robots = []
for line in [l.strip() for l in sys.stdin.readlines()]:
    m = re.match(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)
    robots.append({'px': int(m.group(1)), 'py': int(m.group(2)), 'vx': int(m.group(3)), 'vy': int(m.group(4))})

print('-----')
printgrid(robots)

for r in robots:
    r['px'], r['py'] = r['px'] + r['vx']*100, r['py'] + r['vy']*100
    r['px'] = r['px'] % WIDTH
    r['py'] = r['py'] % HEIGHT
    if r['px'] < 0:
        r['px'] += WIDTH
    if r['py'] < 0:
        r['py'] += HEIGHT

print('=====')
printgrid(robots)

count = [0, 0, 0, 0]
for r in robots:
    if r['px'] < MIDX and r['py'] < MIDY:
        count[0] += 1
    elif r['px'] > MIDX and r['py'] < MIDY:
        count[1] += 1
    elif r['px'] > MIDX and r['py'] > MIDY:
        count[2] += 1
    elif r['px'] < MIDX and r['py'] > MIDY:
        count[3] += 1

print('=====')
print(count)
print(functools.reduce(lambda a, b: a*b, count))
