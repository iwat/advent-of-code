import sys

ready = False
rules = {}
total = 0


def is_valid(elems):
    seen = []
    for e in elems:
        if e in rules:
            afters = rules[e]
            for a in afters:
                if a in seen:
                    return False
        seen.append(e)
    return True


for line in sys.stdin:
    line = line.strip()
    if line == '':
        print(rules)
        ready = True
    else:
        if not ready:
            before, after = line.split('|')
            if before in rules:
                rules[before].append(after)
            else:
                rules[before] = [after]
        else:
            elems = line.split(',')
            if is_valid(elems):
                total += int(elems[(len(elems)-1) >> 1])

print(total)
