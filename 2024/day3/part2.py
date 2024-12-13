import re
import sys

data = sys.stdin.read().strip().replace('\n', ' ')

enabled = True
total = 0
for m in re.finditer(r"(do\(\)|don't\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\))", data):
    if m.group(0) == 'do()':
        enabled = True
    elif m.group(0) == "don't()":
        enabled = False
    elif m.group(0).startswith('mul') and enabled:
        total += int(m.group(2))*int(m.group(3))

print(total)
