import sys
import collections


grid = [list(l.strip()) for l in sys.stdin.readlines() if l.strip() != '']
width = len(grid[0])
height = len(grid)


def find_possible_peaks(x, y):
    q = collections.deque()
    q.appendleft((x - 1, y, 1))
    q.appendleft((x + 1, y, 1))
    q.appendleft((x, y - 1, 1))
    q.appendleft((x, y + 1, 1))

    peaks = set()
    while len(q) > 0:
        next_x, next_y, next_height = q.pop()
        if next_x < 0 or next_y < 0 or next_x >= width or next_y >= height:
            continue
        if grid[next_y][next_x] == str(next_height):
            if next_height == 9:
                peaks.add((next_x, next_y))
            else:
                q.appendleft((next_x - 1, next_y, next_height + 1))
                q.appendleft((next_x + 1, next_y, next_height + 1))
                q.appendleft((next_x, next_y - 1, next_height + 1))
                q.appendleft((next_x, next_y + 1, next_height + 1))
    return peaks


scores = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] != '0':
            continue

        peaks = find_possible_peaks(x, y)
        print(x, y, peaks, len(peaks))
        scores += len(peaks)

print(scores)
