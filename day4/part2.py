#!/usr/bin/env python3
import sys

recent_lines = []
counter = 0

MATRIX = [
         # M         M         A         S         S
        [( 0,  0), ( 2,  0), ( 1, -1), ( 0, -2), ( 2, -2)],
        [( 0, -2), ( 2, -2), ( 1, -1), ( 0,  0), ( 2,  0)],
        [( 0,  0), ( 0, -2), ( 1, -1), ( 2,  0), ( 2, -2)],
        [( 2,  0), ( 2, -2), ( 1, -1), ( 0,  0), ( 0, -2)],
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
        print(' '*x, line[x:x+3], sep='')
    found = 0
    for mm in MATRIX:
        if safe_get(x + mm[0][0], y + mm[0][1]) != 'M':
            continue
        if safe_get(x + mm[1][0], y + mm[1][1]) != 'M':
            continue
        if safe_get(x + mm[2][0], y + mm[2][1]) != 'A':
            continue
        if safe_get(x + mm[3][0], y + mm[3][1]) != 'S':
            continue
        if safe_get(x + mm[4][0], y + mm[4][1]) != 'S':
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

    while len(recent_lines) > 3:
        recent_lines = recent_lines[1:]

    if len(recent_lines) == 3:
        for x in range(len(line)):
            counter += check(x, len(recent_lines)-1, real_y)
    real_y += 1

print(counter)
