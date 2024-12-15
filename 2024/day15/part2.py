import sys


class Box:

    counter = 'A'

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.id = Box.counter
        Box.counter = chr(ord(Box.counter) + 1)
        if Box.counter == '[':
            Box.counter = 'A'

    def try_move(self, dx, dy, grid):
        new_x = self.x + dx
        new_y = self.y + dy
        if grid[new_y][new_x] == '#' or grid[new_y][new_x + 1] == '#':
            return False

        if isinstance(grid[new_y][new_x], Box) and grid[new_y][new_x] != self:
            obj = grid[new_y][new_x]
            if not obj.try_move(dx, dy, grid):
                return False
        if isinstance(grid[new_y][new_x + 1], Box) and grid[new_y][new_x + 1] != self:
            obj = grid[new_y][new_x + 1]
            if not obj.try_move(dx, dy, grid):
                return False

        return True

    def move(self, dx, dy, grid):
        if not self.try_move(dx, dy, grid):
            return

        new_x = self.x + dx
        new_y = self.y + dy
        if grid[new_y][new_x] == '#' or grid[new_y][new_x + 1] == '#':
            return

        ignore = set([self])
        if isinstance(grid[new_y][new_x], Box) and grid[new_y][new_x] not in ignore:
            obj = grid[new_y][new_x]
            obj.move(dx, dy, grid)
            ignore.add(obj)
        if isinstance(grid[new_y][new_x + 1], Box) and grid[new_y][new_x + 1] not in ignore:
            obj = grid[new_y][new_x + 1]
            obj.move(dx, dy, grid)

        if grid[new_y][new_x] in ['.', self] and (grid[new_y][new_x + 1] in ['.', self]):
            grid[self.y][self.x], grid[self.y][self.x + 1] = '.', '.'
            grid[new_y][new_x], grid[new_y][new_x + 1] = self, self
            self.x += dx
            self.y += dy

    def __repr__(self):
        return self.id


lines = [l.strip().replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[.') for l in sys.stdin.readlines()]
blank_line = lines.index('')

grid = [list(l) for l in lines[:blank_line]]
moves = list(''.join(lines[blank_line:]))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '@':
            px, py = x, y
        elif grid[y][x] == '[':
            box = Box(x, y)
            grid[y][x] = box
            grid[y][x + 1] = box

def print_grid(grid, px, py):
    print('\n'.join([''.join([str(c) for c in row]) for row in grid]))


print_grid(grid, px, py)


def move(grid, px, py, dx, dy):
    new_px = px + dx
    new_py = py + dy
    if new_py < 0 or new_py >= len(grid):
        return (px, py)
    if new_px < 0 or new_px >= len(grid[new_py]):
        return (px, py)
    if grid[new_py][new_px] == '#':
        return (px, py)

    # move obstacles
    if isinstance(grid[new_py][new_px], Box):
        grid[new_py][new_px].move(dx, dy, grid)

    # move self
    if grid[new_py][new_px] == '.':
        grid[py][px], grid[new_py][new_px] = grid[new_py][new_px], grid[py][px]
        return (new_px, new_py)
    return (px, py)


for m in moves:
    print('-----')
    print('m:', m)

    if m == '^':
        px, py = move(grid, px, py, 0, -1)
    elif m == '>':
        px, py = move(grid, px, py, 1, 0)
    elif m == 'v':
        px, py = move(grid, px, py, 0, 1)
    elif m == '<':
        px, py = move(grid, px, py, -1, 0)

    print_grid(grid, px, py)

print('=====')
sum_gps = 0
visited = set()
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if isinstance(val, Box) and val not in visited:
            sum_gps += 100 * val.y + val.x
            visited.add(val)

print(sum_gps)
