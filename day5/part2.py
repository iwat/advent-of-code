import functools
import sys

ready = False
rules = {}
reversed_rules = {}
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


def compare(e1, e2):
    if e1 in rules:
        if e2 in rules[e1]:
            return -1
    elif e1 in reversed_rules:
        if e2 in reversed_rules[e1]:
            return 1
    return 0


for line in sys.stdin:
    line = line.strip()
    if line == '':
        ready = True
    else:
        if not ready:
            before, after = line.split('|')
            if before in rules:
                rules[before].append(after)
            else:
                rules[before] = [after]
            if after in reversed_rules:
                reversed_rules[after].append(before)
            else:
                reversed_rules[after] = [before]
        else:
            elems = line.split(',')
            if is_valid(elems):
                pass
            else:
                fixed_elems = sorted(elems, key=functools.cmp_to_key(compare))
                if is_valid(fixed_elems):
                    total += int(fixed_elems[(len(fixed_elems)-1) >> 1])
                else:
                    raise(f'{elems} is invalid')

print(total)
