import collections
import functools
import sys


XY = collections.namedtuple('XY', ['x', 'y'])


class Keypad:
    def __init__(self):
        self.key = 'A'
        self.pos = self._key_to_pos('A')

    def reset(self, c = 'A'):
        self.key = c
        self.pos = self._key_to_pos(c)

    def move(self, d):
        if d == '^':
            self.pos = (self.pos.x, self.pos.y - 1)
        elif d == '>':
            self.pos = (self.pos.x + 1, self.pos.y)
        elif d == 'v':
            self.pos = (self.pos.x, self.pos.y + 1)
        elif d == '<':
            self.pos = (self.pos.x - 1, self.pos.y)
        else:
            raise(BaseException(f'unsupported direction {d}'))
        self.key = self._pos_to_key(self.pos)


class NumericKeypad(Keypad):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """

    KEY_TO_POS = {
            '7': XY(0, 0), '8': XY(1, 0), '9': XY(2, 0),
            '4': XY(0, 1), '5': XY(1, 1), '6': XY(2, 1),
            '1': XY(0, 2), '2': XY(1, 2), '3': XY(2, 2),
                           '0': XY(1, 3), 'A': XY(2, 3),
            }
    POS_TO_KEY = {v: k for k, v in KEY_TO_POS.items()}

    def _key_to_pos(self, c):
        return self.KEY_TO_POS[c]

    def _pos_to_key(self, pos):
        return self.POS_TO_KEY[pos]

    def move_to(self, k):
        if c == self.key:
            return []
        new_pos = self.KEY_TO_POS[k]
        dx, dy = new_pos.x - self.pos.x, new_pos.y - self.pos.y

        options = set()

        if not (self.pos.x == 0 and new_pos.y == 3):
            moves = ''
            if dy < 0:
                moves += '^' * (-dy)
            else:
                moves += 'v' * (dy)
            if dx < 0:
                moves += '<' * (-dx)
            else:
                moves += '>' * (dx)
            options.add(moves)

        if not (self.pos.y == 3 and new_pos.x == 0):
            moves = ''
            if dx < 0:
                moves += '<' * (-dx)
            else:
                moves += '>' * (dx)
            if dy < 0:
                moves += '^' * (-dy)
            else:
                moves += 'v' * (dy)
            options.add(moves)

        self.pos = new_pos
        self.key = k
        return [list(o) for o in options]


class DirectionalKeypad(Keypad):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """

    KEY_TO_POS = {
                           '^': XY(1, 0), 'A': XY(2, 0),
            '<': XY(0, 1), 'v': XY(1, 1), '>': XY(2, 1),
            }
    POS_TO_KEY = {v: k for k, v in KEY_TO_POS.items()}

    def _key_to_pos(self, c):
        return self.KEY_TO_POS[c]

    def _pos_to_key(self, pos):
        return self.POS_TO_KEY[pos]

    def move_to(self, k):
        if k == self.key:
            return [[]]
        new_pos = self.KEY_TO_POS[k]
        dx, dy = new_pos.x - self.pos.x, new_pos.y - self.pos.y

        options = set()

        moves = ''
        if dy > 0:
            moves += 'v'*(dy)
        else:
            moves += '^'*(-dy)
        if dx < 0:
            moves += '<'*(-dx)
        else:
            moves += '>'*(dx)
        options.add(moves)

        if self.key != '<' and k != '<':
            moves = ''
            if dx < 0:
                moves += '<'*(-dx)
            else:
                moves += '>'*(dx)
            if dy > 0:
                moves += 'v'*(dy)
            else:
                moves += '^'*(-dy)
            options.add(moves)

        self.pos = new_pos
        self.key = k
        return [list(o) for o in options]


@functools.cache
def dpad_solve(from_key, to_key, level):
    dpad = DirectionalKeypad()
    dpad.reset(from_key)
    paths = dpad.move_to(to_key)
    if level == 1:
        return min([len(p) for p in paths]) + 1

    min_total = None
    for path in paths:
        path += 'A'
        total = 0
        current = 'A'
        for c in path:
            total += dpad_solve(current, c, level - 1)
            current = c
        if min_total is None or total < min_total:
            min_total = total
    return min_total


score = 0
codes = [l.strip() for l in sys.stdin.readlines()]
for code in codes:
    print('---', code, '---')
    level_1 = []
    numpad = NumericKeypad()
    for c in list(code):
        level_1.append(numpad.move_to(c))
        level_1.append([['A']])

    level_1_combs = []
    q = collections.deque()
    q.append(([], level_1))
    while len(q) > 0:
        cur, more = q.pop()
        if len(more) == 0:
            level_1_combs.append(cur)
            #print('L1:', ''.join(cur))
            continue
        for m in more[0]:
            q.append((cur + m, more[1:]))

    lowest_steps = None
    for level_1 in level_1_combs:
        print('L1:', ''.join(level_1))
        steps = 0
        current_key = 'A'
        for c in level_1:
            steps += dpad_solve(current_key, c, 25)
            current_key = c
        if lowest_steps is None or steps < lowest_steps:
            lowest_steps = steps

    print('L3:', lowest_steps)

    score += lowest_steps * int(code[:-1])

print(score)
