import re
import sys


PATTERN = re.compile(r'([A-Za-z]+) would (lose|gain) ([0-9]+) happiness units by sitting next to ([A-Za-z]+)\.')

pairs = {}
roster = set()

for m in [PATTERN.match(l.strip()) for l in sys.stdin.readlines()]:
    if m.group(2) == 'gain':
        sign = +1
    elif m.group(2) == 'lose':
        sign = -1
    pairs[(m.group(1), m.group(4))] = int(m.group(3)) * sign
    roster.add(m.group(1))


def calculate(order):
    if len(order) == len(roster):
        total_emo = 0
        for i in range(len(order)):
            left = (i + len(order) - 1) % len(order)
            right = (i + 1) % len(order)
            left_emo = pairs[(order[i], order[left])]
            right_emo = pairs[(order[i], order[right])]
            print(order[left], left_emo, '->', order[i], '<-', right_emo, order[right])
            total_emo += left_emo + right_emo
        return total_emo


    best_outcome = 0
    for person in roster:
        if person not in order:
            outcome = calculate(order + [person])
            if outcome > best_outcome:
                best_outcome = outcome
    return best_outcome


print(calculate([]))
