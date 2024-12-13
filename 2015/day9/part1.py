import re
import sys

cities = set()
links = {}

for line in [l.strip() for l in sys.stdin.readlines()]:
    m = re.match(r'([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)', line)
    loc1 = m.group(1)
    loc2 = m.group(2)
    dist = int(m.group(3))
    links[(loc1, loc2)] = dist
    links[(loc2, loc1)] = dist
    cities.add(loc1)
    cities.add(loc2)

def find_route(visited, dist):
    if len(visited) == len(cities):
        print(visited, dist)
        return dist

    shortest = None
    for c in cities:
        if c in visited:
            continue
        route = None
        if len(visited) == 0:
            route = find_route([c], 0)
        elif (visited[-1], c) in links:
            route = find_route(visited + [c], dist + links[(visited[-1], c)])
        if route is not None:
            if shortest is None or route < shortest:
                shortest = route
    return shortest

shortest = find_route([], 0)

print('=====')
print(shortest)
