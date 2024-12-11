import sys

DEBUG = False

stones = [{'val': int(s), 'round': -1} for s in sys.stdin.read().strip().split(' ')]

first_stone = stones[0]
last_stone = stones[0]

first_stone['next'] = None
first_stone['prev'] = None

for s in stones[1:]:
    s['next'] = None
    s['prev'] = last_stone
    last_stone['next'] = s
    last_stone = s

for r in range(25):
    current_stone = first_stone
    while current_stone is not None:
        if current_stone['round'] == r:
            current_stone = current_stone['next']
            continue

        current_stone['round'] = r
        if current_stone['val'] == 0:
            current_stone['val'] = 1
        elif len(str(current_stone['val'])) % 2 == 0:
            strval = str(current_stone['val'])
            left = int(strval[:(len(strval) >> 1)])
            right = int(strval[(len(strval) >> 1):])
            current_stone['val'] = left
            new_stone = {'round': r, 'val': right, 'prev': current_stone, 'next': current_stone['next']}
            current_stone['next'] = new_stone
        else:
            current_stone['val'] *= 2024
    if DEBUG:
        current_stone = first_stone
        while current_stone is not None:
            print(current_stone['val'], end=' ')
            current_stone = current_stone['next']
        print()

if DEBUG:
    current_stone = first_stone
    while current_stone is not None:
        print(current_stone['val'], end=' ')
        current_stone = current_stone['next']
    print()

stones = 0
current_stone = first_stone
while current_stone is not None:
    stones += 1
    current_stone = current_stone['next']

print(stones)
