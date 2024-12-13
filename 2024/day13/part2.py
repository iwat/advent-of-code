import collections
import heapq
import sys
import time
import re

total_cost = 0
while line := sys.stdin.readline().strip():
    ma = re.match(r'Button A: X([+-][0-9]+), Y([+-][0-9]+)', line)
    mb = re.match(r'Button B: X([+-][0-9]+), Y([+-][0-9]+)', sys.stdin.readline().strip())
    mp = re.match(r'Prize: X=([0-9]+), Y=([0-9]+)', sys.stdin.readline().strip())
    _ = sys.stdin.readline().strip()

    ax = int(ma.group(1))
    ay = int(ma.group(2))
    bx = int(mb.group(1))
    by = int(mb.group(2))
    px = int(mp.group(1)) + 10000000000000
    py = int(mp.group(2)) + 10000000000000

    slope_a, intercept_a = ay / ax, 0
    slope_b = by / bx
    intercept_b = py - (slope_b * px)

    print('-----')
    print('p:', (px, py))
    print('a:', (ax, ay), 's:', slope_a, 'c:', intercept_a)
    print('b:', (bx, by), 's:', slope_b, 'c:', intercept_b)

    intersect_x = (intercept_b - intercept_a) / (slope_a - slope_b)
    intersect_y = (slope_a * intersect_x) + intercept_a

    print('i:', (intersect_x, intersect_y))

    tok_a = round(min(intersect_x / ax, intersect_y / ay))
    tok_b = round(min((px - intersect_x) / bx, (py - intersect_y) / by))

    if px == ax*tok_a + bx*tok_b and py == ay*tok_a + by*tok_b:
        print('ta:', tok_a)
        print('tb:', tok_b)
        total_cost += tok_a*3 + tok_b


print('=====')
print(total_cost)
