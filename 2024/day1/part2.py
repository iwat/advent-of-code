import re
import sys

left = []
right = {}

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l, r = re.split(r'\s+', line)
    left.append(int(l))
    right[int(r)] = right.get(int(r), 0) + 1

score = 0
for l in left:
    score += l * right.get(l, 0)

print(score)
