import sys

total_need = 0
for line in sys.stdin.readlines():
    w, h, d = line.strip().split('x')
    w, h, d = int(w), int(h), int(d)
    dims = sorted([w, h, d])
    need = 2*dims[0] + 2*dims[1]
    need += w*h*d
    total_need += need

print(total_need)
