import sys


available = sys.stdin.readline().strip().split(', ')
print(available)


def solve(current, design):
    remaining = design[len(current):]
    if len(remaining) == 0:
        return current == design

    for a in available:
        if remaining[0:len(a)] == a:
            if solve(current + a, design):
                return True
    return False


possibilities = []
for design in [l.strip() for l in sys.stdin.readlines() if l != '\n']:
    if solve('', design):
        print(design)
        possibilities.append(design)

print(len(possibilities))
