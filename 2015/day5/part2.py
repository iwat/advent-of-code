import sys

good = 0
for line in [l.strip() for l in sys.stdin.readlines()]:
    double = False
    for i in range(len(line) - 1):
        two = line[i:i+2]
        try:
            line.index(two, i+2)
            double = True
            break
        except ValueError:
            pass
    if not double:
        continue

    repeat = False
    for i in range(1, len(line) - 1):
        if line[i-1] == line[i+1]:
            repeat = True
            break
    if not repeat:
        continue

    print(line)
    good += 1

print(good)
