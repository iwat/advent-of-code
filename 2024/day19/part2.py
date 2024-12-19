import sys


available = sys.stdin.readline().strip().split(', ')
print(available)


memo = {}
def solve(current, design):
    if (current, design) in memo:
        return memo[(current, design)]

    remaining = design[len(current):]
    if len(remaining) == 0:
        if current == design:
            memo[(current, design)] = 1
            return 1
        memo[(current, design)] = 0
        return 0

    possibilities = 0
    for a in available:
        if remaining[0:len(a)] == a:
            possibilities += solve(current + a, design)

    memo[(current, design)] = possibilities
    return possibilities


possibilities = 0
for design in [l.strip() for l in sys.stdin.readlines() if l != '\n']:
    p = solve('', design)
    print(design, p)
    possibilities += p

print(possibilities)
