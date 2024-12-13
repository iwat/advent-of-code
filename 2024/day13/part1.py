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

    ax = int(ma.group(1))
    ay = int(ma.group(2))
    bx = int(mb.group(1))
    by = int(mb.group(2))
    px = int(mp.group(1))
    py = int(mp.group(2))

    print(ax, ay, bx, by, px, py)

    costs = {}
    heap = [(0, 0, 0)]
    while len(heap) > 0:
        t, x, y = heapq.heappop(heap)
        if x > px or y > py:
            continue
        if (x, y) not in costs or t < costs[(x, y)]:
            costs[(x, y)] = t
            heapq.heappush(heap, (t+3, x+ax, y+ay))
            heapq.heappush(heap, (t+1, x+bx, y+by))

    empty = sys.stdin.readline().strip()
    cost = costs.get((px, py))
    print(cost)
    if cost is not None:
        total_cost += cost

print(total_cost)
