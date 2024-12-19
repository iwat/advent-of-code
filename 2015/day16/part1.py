import sys

goal = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
        }

for no, props in [l.strip().split(': ', 1) for l in sys.stdin.readlines()]:
    props = dict([p.split(': ') for p in props.split(', ')])
    for k, v in props.items():
        props[k] = int(v)
    diff = dict([(k, v - goal[k]) for k, v in props.items()])
    delta = set(diff.values())

    if len(delta) == 1 and delta.pop() == 0:
        print(no, props, delta, diff, '!!!!!')
