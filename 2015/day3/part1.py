import sys

houses = set()
houses.add((0, 0))

cur_x = 0
cur_y = 0

for direction in list(sys.stdin.readline().strip()):
    if direction == '>':
        cur_x += 1
    elif direction == 'v':
        cur_y += 1
    elif direction == '<':
        cur_x -= 1
    elif direction == '^':
        cur_y -= 1

    houses.add((cur_x, cur_y))

print(len(houses))
