import sys


storage = int(sys.argv[1])
containers = [int(l.strip()) for l in sys.stdin.readlines()]


def possibilities(idxs):
    remaining = storage - sum([containers[i] for i in idxs])
    if remaining == 0:
        print(idxs, [containers[i] for i in idxs])
        return 1
    if remaining < 0:
        return 0

    min_idx = 0
    if len(idxs) > 0:
        min_idx = idxs[-1]
    poss = 0
    for i in range(min_idx, len(containers)):
        if i  in idxs:
            continue
        poss += possibilities(idxs + [i])
    return poss


print(possibilities([]))
