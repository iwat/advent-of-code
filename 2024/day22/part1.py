import collections
import sys


def solve(initial, rounds):
    for r in range(rounds):
        v1 = initial * 64
        initial ^= v1
        initial %= 16777216

        v2 = initial // 32
        initial ^= v2
        initial %= 16777216

        v3 = initial * 2048
        initial ^= v3
        initial %= 16777216

    return initial


result = 0
for line in [l.strip() for l in sys.stdin.readlines()]:
    sol = solve(int(line), 2000)
    print(f'{line}: {sol}')
    result += sol

print(result)
