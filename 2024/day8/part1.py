import sys
import time


grid = [list(l.strip()) for l in sys.stdin.readlines() if l.strip() != '']
width = len(grid[0])
height = len(grid)

antinodes = [['.' for _ in range(width)] for _ in range(height)]
antennas = {}

for x in range(width):
    for y in range(height):
        if grid[y][x] != '.':
            if grid[y][x] in antennas:
                antennas[grid[y][x]].append((x, y))
            else:
                antennas[grid[y][x]] = [(x, y)]

print('\n'.join([''.join(row) for row in grid]))
print()

for name, ans in antennas.items():
    for an1 in ans:
        for an2 in ans:
            if an2 == an1:
                continue
            vector = (an2[0] - an1[0], an2[1] - an1[1])
            antinode = (an2[0] + vector[0], an2[1] + vector[1])
            if antinode[0] < 0 or antinode[0] >= width:
                continue
            if antinode[1] < 0 or antinode[1] >= height:
                continue
            print(name, an1, an2, vector, antinode)
            antinodes[antinode[1]][antinode[0]] = '#'
print()

print('\n'.join([''.join(row) for row in antinodes]))
print()

print(len([cell for row in antinodes for cell in row if cell == '#']))
