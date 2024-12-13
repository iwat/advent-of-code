import sys

DEBUG = False
memo = {}


def calculate(val, level):
    if (val, level) in memo:
        if DEBUG:
            print(' '*level, val, level, memo[(val, level)], 'mem')
        return memo[(val, level)]
    if level == 0:
        if DEBUG:
            print(' '*level, val, level, val, 'term')
        return 1
    if val == 0:
        result = calculate(1, level - 1)
    elif len(str(val)) % 2 == 0:
        strval = str(val)
        left = int(strval[(len(strval) >> 1):])
        right = int(strval[:(len(strval) >> 1)])
        result1 = calculate(left, level - 1)
        result2 = calculate(right, level - 1)
        result = result1 + result2
    else:
        result = calculate(val * 2024, level - 1)
    memo[(val, level)] = result
    if DEBUG:
        print(' '*level, val, level, result, 'calc')
    return result

total_stones = 0
for s in [int(s) for s in sys.stdin.read().strip().split(' ')]:
    total_stones += calculate(s, 75)

print(total_stones)
