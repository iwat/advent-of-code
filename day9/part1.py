import sys

is_space = False
file_id = 0
blocks = []

for c in sys.stdin.read():
    if c == '' or c == '\n':
        continue
    read_blocks = int(c)
    if is_space:
        blocks.extend(['.' for _ in range(read_blocks)])
    else:
        blocks.extend([file_id for _ in range(read_blocks)])
        file_id += 1
    is_space = not is_space

print(''.join([str(b) for b in blocks]))

file_cursor = len(blocks) - 1
space_cursor = 0
while True:
    if space_cursor >= len(blocks):
        break
    if file_cursor < 0:
        break
    #print(file_cursor, blocks[file_cursor], space_cursor, blocks[space_cursor])
    if blocks[space_cursor] != '.':
        space_cursor += 1
        continue
    if blocks[file_cursor] == '.':
        file_cursor -= 1
        continue
    if file_cursor < space_cursor:
        break
    blocks[space_cursor], blocks[file_cursor] = blocks[file_cursor], blocks[space_cursor]
    space_cursor += 1
    file_cursor -= 1
    #print(''.join([str(b) for b in blocks]))

print(''.join([str(b) for b in blocks]))

print(sum([c*i for i, c in enumerate(blocks) if c != '.']))
