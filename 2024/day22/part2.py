import collections
import sys


def solve(secret, rounds):
    price_map = {}
    deltas = []
    prev_price = secret % 10
    for r in range(rounds):
        v1 = secret * 64
        secret ^= v1
        secret %= 16777216

        v2 = secret // 32
        secret ^= v2
        secret %= 16777216

        v3 = secret * 2048
        secret ^= v3
        secret %= 16777216

        price = (secret % 10)
        delta = price - prev_price
        prev_price = price
        deltas.append(delta)
        if len(deltas) >= 4:
            key = tuple(deltas[-4:])
            if key not in price_map:
                price_map[key] = price

    return price_map


master_price_map = {}
for line in [l.strip() for l in sys.stdin.readlines()]:
    price_map = solve(int(line), 2000)
    #print(f'{line}:')
    top_price = sorted(price_map.items(), key=lambda kv: kv[1])
    #for k, v in top_price:
    #    print(k, v)
    for k, v in price_map.items():
        if k in master_price_map:
            master_price_map[k] += v
        else:
            master_price_map[k] = v

print(sorted(master_price_map.items(), key=lambda kv: kv[1]))
