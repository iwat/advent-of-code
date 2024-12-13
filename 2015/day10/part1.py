line = list('1321131112')

for i in range(40):
    print(f'{i}:', len(line))
    new_line = []

    current = line[0]
    count = 1
    for c in line[1:]:
        if c == current:
            count += 1
        else:
            new_line.extend([count, current])
            current = c
            count = 1
    new_line.extend([count, current])
    line = [str(c) for c in new_line]

print(f'{i + 1}:', len(line))
