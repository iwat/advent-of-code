import sys

code_bytes = 0
mem_bytes = 0
for line in [l.strip() for l in sys.stdin.readlines()]:
    code_bytes += len(line)
    actual = eval(line)
    print(line, '->', actual)
    mem_bytes += len(actual)

print('c:', code_bytes)
print('a:', mem_bytes)
print('d:', code_bytes - mem_bytes)
