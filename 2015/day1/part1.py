import sys

data = list(sys.stdin.read().strip())

floor = 0
for d in data:
    if d == '(':
        floor += 1
    elif d == ')':
        floor -= 1
    else:
        raise(BaseException(f'unsupported {d}'))

print(floor)
