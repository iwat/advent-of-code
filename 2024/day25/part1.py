import sys


def solve(locks, keys):
    unique_pairs = set()
    for l in locks:
        for k in keys:
            overlaps = [
                    l[0] + k[0] - 5,
                    l[1] + k[1] - 5,
                    l[2] + k[2] - 5,
                    l[3] + k[3] - 5,
                    l[4] + k[4] - 5,
                    ]
            # too big
            if max(overlaps) > 0:
                continue
            unique_pairs.add((l, k))
    return unique_pairs



def main():
    lines = [l.strip() for l in sys.stdin.readlines()]

    keys = []
    locks = []

    for ndx in range(0, len(lines), 8):
        if lines[ndx] == '#####':
            sch_type = 'lock'
        else:
            sch_type = 'key'
        sch_heights = [0] * 5

        for line in lines[ndx + 1:ndx + 6]:
            for i, c in enumerate(list(line)):
                if c == '#':
                    sch_heights[i] += 1

        if sch_type == 'lock':
            locks.append(tuple(sch_heights))
        else:
            keys.append(tuple(sch_heights))

    unique_pairs = solve(locks, keys)
    print('=====')
    for p in unique_pairs:
        print(p[0], p[1])
    print('len:', len(unique_pairs))


if __name__ == '__main__':
    main()
