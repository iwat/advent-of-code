#!/usr/bin/env python3
import sys

recent_lines = []
counter = 0

MATRIX = [
        [( 0,  0), ( 1,  0), ( 2,  0), ( 3,  0)],
        [( 0,  0), (-1,  0), (-2,  0), (-3,  0)],
        [( 0,  0), ( 1, -1), ( 2, -2), ( 3, -3)],
        [( 3, -3), ( 2, -2), ( 1, -1), ( 0,  0)],
        [( 0,  0), ( 0, -1), ( 0, -2), ( 0, -3)],
        [( 0, -3), ( 0, -2), ( 0, -1), ( 0,  0)],
        [(-3, -3), (-2, -2), (-1, -1), ( 0,  0)],
        [( 0,  0), (-1, -1), (-2, -2), (-3, -3)],
        ]

def safe_get(x, y):
    if y < 0 or y >= len(recent_lines):
        return ''
    if x < 0 or x >= len(recent_lines[y]):
        return ''
    return recent_lines[y][x]

def check(x, y, real_y):
    print(f'-----({x},{real_y})-------')
    for line in recent_lines:
        print(' '*max(0,x-4), line[max(0,x-4):min(x+4,len(line))], sep='')
    found = 0
    for mm in MATRIX:
        if safe_get(x + mm[0][0], y + mm[0][1]) != 'X':
            continue
        if safe_get(x + mm[1][0], y + mm[1][1]) != 'M':
            continue
        if safe_get(x + mm[2][0], y + mm[2][1]) != 'A':
            continue
        if safe_get(x + mm[3][0], y + mm[3][1]) != 'S':
            continue
        print((x + mm[0][0], real_y + mm[0][1]), mm)
        found += 1
    return found

real_y = 0
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break

    recent_lines.append(line)

    if len(recent_lines) >= 5:
        recent_lines = recent_lines[1:]

    for x in range(len(line)):
        counter += check(x, len(recent_lines)-1, real_y)
    real_y += 1

print(counter)

#   0123456789
# 0 ....XXMAS. (4,0) (5,0)
# 1 .SAMXMS... (4,1)
# 2 ...S..A...
# 3 ..A.A.MS.X (9,3)
# 4 XMASAMX.MM (0,4) (6,4)
# 5 X.....XA.A (0,5) (6,5)
# 6 S.S.S.S.SS
# 7 .A.A.A.A.A
# 8 ..M.M.M.MM
# 9 .X.X.XMASX
