import sys
import collections


XY = collections.namedtuple('XY', ['x', 'y'])


grid = [list(l.strip()) for l in sys.stdin.readlines() if l.strip() != '']
width = len(grid[0])
height = len(grid)

coordinates = set([XY(x, y) for x in range(width) for y in range(height)])
regions = []
while len(coordinates) > 0:
    q = collections.deque()
    q.append(coordinates.pop())
    cells = []
    while len(q) > 0:
        c = q.pop()
        cells.append(c)

        if c.x > 0:
            left = XY(c.x - 1, c.y)
            if grid[left.y][left.x] == grid[c.y][c.x] and left in coordinates:
                coordinates.remove(left)
                q.append(left)
        if c.x < width - 1:
            right = XY(c.x + 1, c.y)
            if grid[right.y][right.x] == grid[c.y][c.x] and right in coordinates:
                coordinates.remove(right)
                q.append(right)
        if c.y > 0:
            up = XY(c.x, c.y - 1)
            if grid[up.y][up.x] == grid[c.y][c.x] and up in coordinates:
                coordinates.remove(up)
                q.append(up)
        if c.y < height - 1:
            down = XY(c.x, c.y + 1)
            if grid[down.y][down.x] == grid[c.y][c.x] and down in coordinates:
                coordinates.remove(down)
                q.append(down)
    regions.append(cells)

total_cost = 0
for r in regions:
    print('-----')
    print(r)
    print('t:', grid[r[0].y][r[0].x])

    perimeter = 0
    cells = set(r)
    for c in r:
        if XY(c.x - 1, c.y) not in cells:
            print(' +', c, XY(c.x - 1, c.y))
            perimeter += 1
        if XY(c.x, c.y - 1) not in cells:
            print(' +', c, XY(c.x, c.y - 1))
            perimeter += 1
        if XY(c.x + 1, c.y) not in cells:
            print(' +', c, XY(c.x + 1, c.y))
            perimeter += 1
        if XY(c.x, c.y + 1) not in cells:
            print(' +', c, XY(c.x, c.y + 1))
            perimeter += 1

    print('a:', len(r))
    print('p:', perimeter)
    print('c:', perimeter * len(r))
    total_cost += perimeter * len(r)

print('=====')
print(total_cost)
