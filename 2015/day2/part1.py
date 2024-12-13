import sys

total_need = 0
for line in sys.stdin.readlines():
    w, h, d = line.strip().split('x')
    area1 = int(w)*int(h)
    area2 = int(w)*int(d)
    area3 = int(h)*int(d)
    extra = min(area1, area2, area3)
    need = 2*area1 + 2*area2 + 2*area3 + extra
    total_need += need

print(total_need)
