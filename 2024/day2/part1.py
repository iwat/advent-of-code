import sys


def is_safe(levels):
    if levels[0] == levels[1]:
        return False
    if levels[1] > levels[0]:
        direction = 1
    else:
        direction = -1

    recent = levels[0]
    for l in levels[1:]:
        diff = (l - recent) * direction
        if diff < 1 or diff > 3:
            return False
        recent = l
    return True


safe = 0
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    levels = [int(c) for c in line.split(' ')]
    if is_safe(levels):
        safe += 1
print(safe)
