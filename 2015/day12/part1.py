import json
import sys

def count(obj):
    total = 0
    if isinstance(obj, dict):
        for v in obj.values():
            total += count(v)
    elif isinstance(obj, list):
        for v in obj:
            total += count(v)
    elif isinstance(obj, int) or isinstance(obj, float):
        total += obj
    return total


obj = json.load(sys.stdin)
print(count(obj))
