import collections
import sys

ingredients = {}
for line in [l.strip() for l in sys.stdin.readlines()]:
    ingredient, properties = line.split(': ')
    properties = dict([kv.split(' ') for kv in properties.split(', ')])
    for k, v in properties.items():
        properties[k] = int(v)
    ingredients[ingredient] = properties


def calculate(mixes):
    #print('-----')
    #print(mixes)

    props = None
    for ing, amt in mixes.items():
        if props is None:
            props = dict([(p, v*amt) for p, v in ingredients[ing].items()])
        else:
            new_props = dict([(p, v*amt) for p, v in ingredients[ing].items()])
            for p, v in new_props.items():
                props[p] += v

    calories = props['calories']
    del props['calories']

    #print(props)
    score = 1
    for v in props.values():
        if v < 0:
            score = 0
        else:
            score *= v
    #print(score)
    if calories != 500:
        return 0

    return score


highest_score = 0
highest_mixes = None

q = collections.deque()
q.append({})
while len(q) > 0:
    mixes = q.pop()
    if len(mixes) == len(ingredients):
        score = calculate(mixes)
        if score > highest_score:
            highest_score = score
            highest_mixes = mixes
        continue
    used = sum(mixes.values())
    for ing in ingredients.keys():
        if ing in mixes:
            continue
        if len(mixes) + 1 == len(ingredients):
            q.append(mixes | {ing: 100 - used})
        else:
            for amount in range(100 - used, -1, -1):
                q.append(mixes | {ing: amount})

print('=====')
print(highest_score)
print(highest_mixes)
