import re
import sys

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in [l.strip() for l in sys.stdin.readlines()]:
    m = re.match(r'(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line)
    for x in range(int(m.group(2)), int(m.group(4)) + 1):
        for y in range(int(m.group(3)), int(m.group(5)) + 1):
            if m.group(1) == 'toggle':
                grid[y][x] += 2
            elif m.group(1) == 'turn on':
                grid[y][x] += 1
            elif m.group(1) == 'turn off':
                if grid[y][x] > 0:
                    grid[y][x] -= 1

print(sum([c for r in grid for c in r]))
