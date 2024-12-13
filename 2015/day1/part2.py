import sys

data = list(sys.stdin.read().strip())

floor = 0
for ndx, d in enumerate(data):
    if d == '(':
        floor += 1
    elif d == ')':
        floor -= 1
    else:
        raise(BaseException(f'unsupported {d}'))
    if floor == -1:
        print(ndx + 1)
        break
