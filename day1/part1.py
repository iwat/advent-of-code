import re
import sys

left = []
right = []

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l, r = re.split(r'\s+', line)
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

diff = 0
for i in range(len(left)):
    diff += abs(right[i] - left[i])

print(diff)
