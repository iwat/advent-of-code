import sys

code_bytes = 0
mem_bytes = 0
for line in [l.strip() for l in sys.stdin.readlines()]:
    mem_bytes += len(line)
    encoded = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
    print(line, len(line), '->', encoded, len(encoded))
    code_bytes += len(encoded)

print('c:', code_bytes)
print('a:', mem_bytes)
print('d:', code_bytes - mem_bytes)
