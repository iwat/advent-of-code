import sys

lines = [l.strip() for l in sys.stdin.readlines()]
blank_line = lines.index('')

grid = [list(l) for l in lines[:blank_line]]
moves = list(''.join(lines[blank_line:]))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '@':
            px, py = x, y
            break

def print_grid(grid, px, py):
    print('\n'.join([''.join(row) for row in grid]))


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
    if grid[new_py][new_px] == 'O':
        move(grid, new_px, new_py, dx, dy)

    # move self
    if grid[new_py][new_px] == '.':
        grid[py][px], grid[new_py][new_px] = grid[new_py][new_px], grid[py][px]
        return (new_px, new_py)
    return (px, py)


for m in moves:
    if m == '^':
        px, py = move(grid, px, py, 0, -1)
    elif m == '>':
        px, py = move(grid, px, py, 1, 0)
    elif m == 'v':
        px, py = move(grid, px, py, 0, 1)
    elif m == '<':
        px, py = move(grid, px, py, -1, 0)

    print('-----')
    print('m:', m)
    print_grid(grid, px, py)

print('=====')
sum_gps = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == 'O':
            sum_gps += 100 * y + x

print(sum_gps)
