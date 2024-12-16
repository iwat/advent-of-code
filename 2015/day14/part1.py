import collections
import re
import sys


Reindeer = collections.namedtuple('Reindeer', ['name', 'speed', 'duration', 'rest'])
DURATION = 2503
PATTERN = re.compile(r'([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds\.')

reindeer = []
for m in [PATTERN.match(l.strip()) for l in sys.stdin.readlines()]:
    name, speed, duration, rest = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    reindeer.append(Reindeer(name, speed, duration, rest))

best = None
for r in reindeer:
    cycle_time = r.duration + r.rest
    cycles = int(DURATION / cycle_time)

    cycle_distance = cycles * r.speed * r.duration
    remaining_secs = DURATION - cycles * cycle_time
    if remaining_secs > r.duration:
        remaining_secs = r.duration

    additional_distance = remaining_secs * r.speed
    total_distance = cycle_distance + additional_distance
    print(r, cycles, cycle_distance, additional_distance, total_distance)

    if best is None or best[1] < total_distance:
        best = (r, total_distance)

print('=====')
print(best)
