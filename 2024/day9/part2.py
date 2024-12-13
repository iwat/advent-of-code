import sys

is_space = False
file_id = 0
objects = []

for c in sys.stdin.read():
    if c == '' or c == '\n':
        continue
    object_size = int(c)
    if is_space:
        objects.append({'id':'.', 'size': object_size})
    else:
        objects.append({'id':file_id, 'size': object_size})
        file_id += 1
    is_space = not is_space

print(objects)

file_cursor = len(objects) - 1
while True:
    if file_cursor < 0:
        break
    if objects[file_cursor]['id'] == '.':
        file_cursor -= 1
        continue
    if 'moved' in objects[file_cursor]:
        file_cursor -= 1
        continue

    moved = False
    space_cursor = 0
    while True:
        if space_cursor >= len(objects):
            break
        if objects[space_cursor]['id'] != '.':
            space_cursor += 1
            continue
        if file_cursor < space_cursor:
            break

        print(file_cursor, objects[file_cursor], space_cursor, objects[space_cursor])
        if objects[file_cursor]['size'] == objects[space_cursor]['size']:
            objects[file_cursor]['moved'] = True
            objects[space_cursor], objects[file_cursor] = objects[file_cursor], objects[space_cursor]
            file_cursor -= 1
            moved = True
            break
        elif objects[file_cursor]['size'] < objects[space_cursor]['size']:
            objects[file_cursor]['moved'] = True
            space2 = {'id': '.', 'size': objects[space_cursor]['size'] - objects[file_cursor]['size']}
            objects[space_cursor]['size'] = objects[file_cursor]['size']
            objects[space_cursor], objects[file_cursor] = objects[file_cursor], objects[space_cursor]
            objects.insert(space_cursor + 1, space2)
            moved = True
            break
        else:
            space_cursor += 1

    if not moved:
        file_cursor -= 1

print(objects)

check = 0
cursor = 0
for o in objects:
    if o['id'] != '.':
        for i in range(o['size']):
            check += (cursor + i)*o['id']
    cursor += o['size']

print(check)
