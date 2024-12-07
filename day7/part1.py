import collections
import sys

calibration = 0
for line in sys.stdin:
    goal, nums = line.strip().split(':')
    goal = int(goal)
    nums = [int(n) for n in nums.strip().split(' ')]

    q = collections.deque()
    q.append((nums[0], '+', nums[1:], f'{nums[0]}+{nums[1]}'))
    q.append((nums[0], '*', nums[1:], f'{nums[0]}*{nums[1]}'))

    while len(q) > 0:
        state = q.pop()
        if state[1] == '+':
            val = state[0] + state[2][0]
        elif state[1] == '*':
            val = state[0] * state[2][0]
        if len(state[2]) == 1:
            if val == goal:
                print(goal, '=', state[3])
                calibration += goal
                break
        else:
            q.append((val, '+', state[2][1:], f'{state[3]}+{state[2][1]}'))
            q.append((val, '*', state[2][1:], f'{state[3]}+{state[2][1]}'))

print(calibration)
