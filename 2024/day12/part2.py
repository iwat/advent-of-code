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
for cells in regions:
    print('-----')
    print(cells)
    print('t:', grid[cells[0].y][cells[0].x])

    perimeters = {}
    cell_set = set(cells)
    for c in cells:
        if XY(c.x - 1, c.y) not in cell_set:
            perimeters[(c, 'l')] = None
        if XY(c.x, c.y - 1) not in cell_set:
            perimeters[(c, 't')] = None
        if XY(c.x + 1, c.y) not in cell_set:
            perimeters[(c, 'r')] = None
        if XY(c.x, c.y + 1) not in cell_set:
            perimeters[(c, 'b')] = None

    print('a:', len(cells))
    print('p:', perimeters.keys())

    lines = []
    for xyd  in perimeters.keys():
        if perimeters[xyd] is not None:
            raise(BaseException('weird'))
            continue
        xy, d = xyd
        if d == 't' or d == 'b':
            dx = 1
            dy = 0
        elif d == 'l' or d == 'r':
            dy = 1
            dx = 0

        neighbor1 = (XY(xy.x - dx, xy.y - dy), d)
        if neighbor1 in perimeters and perimeters[neighbor1] is not None:
            perimeters[xyd] = perimeters[neighbor1]
            perimeters[xyd].append(xyd)

        neighbor2 = (XY(xy.x + dx, xy.y + dy), d)
        if neighbor2 in perimeters and perimeters[neighbor2] is not None:
            if perimeters[xyd] is not None and perimeters[xyd] != perimeters[neighbor2]:
                old_line = perimeters[neighbor2]
                for r_xyd in old_line:
                    perimeters[xyd].append(r_xyd)
                    perimeters[r_xyd] = perimeters[xyd]
                lines.remove(old_line)
            else:
                perimeters[xyd] = perimeters[neighbor2]
                perimeters[xyd].append(xyd)
        if perimeters[xyd] is None:
            new_line = [xyd]
            perimeters[xyd] = new_line
            lines.append(new_line)

    for l in lines:
        print('l:', l)

    print('l:', len(lines))
    print('c:', len(lines) * len(cells))
    total_cost += len(lines) * len(cells)

print("=====")
print(total_cost)
