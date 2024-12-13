import sys

good = 0
for line in [l.strip() for l in sys.stdin.readlines()]:
    chars = list(line)

    vowels = 0
    for c in chars:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
            if vowels == 3:
                break
    if vowels < 3:
        continue

    double = False
    for i in range(len(line)-1):
        if chars[i] == chars[i+1]:
            double = True
            break
    if not double:
        continue

    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        continue

    print(line)
    good += 1

print(good)
