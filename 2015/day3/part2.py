import sys

houses = set()
houses.add((0, 0))

santa = 0
cur_x = [0, 0]
cur_y = [0, 0]

for direction in list(sys.stdin.readline().strip()):
    if direction == '>':
        cur_x[santa] += 1
    elif direction == 'v':
        cur_y[santa] += 1
    elif direction == '<':
        cur_x[santa] -= 1
    elif direction == '^':
        cur_y[santa] -= 1

    houses.add((cur_x[santa], cur_y[santa]))
    santa = (santa + 1) % 2

print(len(houses))
