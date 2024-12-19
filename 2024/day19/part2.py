import functools
import sys


available = sys.stdin.readline().strip().split(', ')
print(available)


@functools.cache
def solve(current, design):
    remaining = design[len(current):]
    if len(remaining) == 0:
        if current == design:
            return 1
        return 0

    possibilities = 0
    for a in available:
        if remaining[0:len(a)] == a:
            possibilities += solve(current + a, design)

    return possibilities


possibilities = 0
for design in [l.strip() for l in sys.stdin.readlines() if l != '\n']:
    p = solve('', design)
    print(design, p)
    possibilities += p

print(possibilities)
