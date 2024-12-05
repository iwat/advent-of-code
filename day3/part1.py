import re
import sys

data = sys.stdin.read().strip().replace('\n', ' ')

total = 0
for m in re.finditer(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', data):
    total += int(m.group(1))*int(m.group(2))

print(total)
