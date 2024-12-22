import collections
import sys


class Keypad:
    def __init__(self):
        self.key = 'A'
        self.pos = self._key_to_pos('A')

    def reset(self, c = 'A'):
        self.key = c
        self.pos = self._key_to_pos(c)

    def move(self, d):
        if d == '^':
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif d == '>':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif d == 'v':
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif d == '<':
            self.pos = (self.pos[0] - 1, self.pos[1])
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
            '7': (0, 0), '8': (1, 0), '9': (2, 0),
            '4': (0, 1), '5': (1, 1), '6': (2, 1),
            '1': (0, 2), '2': (1, 2), '3': (2, 2),
                         '0': (1, 3), 'A': (2, 3),
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
        dx, dy = new_pos[0] - self.pos[0], new_pos[1] - self.pos[1]

        options = []

        if not (self.pos[0] == 0 and new_pos[1] == 3):
            moves = []
            if dy < 0:
                moves += ['^'] * (-dy)
            else:
                moves += ['v'] * (dy)
            if dx < 0:
                moves += ['<'] * (-dx)
            else:
                moves += ['>'] * (dx)
            options.append(moves)
            print('1:', self.pos[0], new_pos[1], moves)

        if not (self.pos[1] == 3 and new_pos[0] == 0):
            moves = []
            if dx < 0:
                moves += ['<'] * (-dx)
            else:
                moves += ['>'] * (dx)
            if dy < 0:
                moves += ['^'] * (-dy)
            else:
                moves += ['v'] * (dy)
            options.append(moves)
            print('2:', self.pos[1], new_pos[0], moves)

        self.pos = new_pos
        self.key = k
        return options


class DirectionalKeypad(Keypad):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """

    KEY_TO_POS = {
                         '^': (1, 0), 'A': (2, 0),
            '<': (0, 1), 'v': (1, 1), '>': (2, 1),
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
        dx, dy = new_pos[0] - self.pos[0], new_pos[1] - self.pos[1]
        self.pos = new_pos
        self.key = k

        moves = []
        if dy > 0:
            moves += 'v'*(dy)
        if dx > 0:
            moves += '>'*(dx)
        if dy < 0:
            moves += '^'*(-dy)
        if dx < 0:
            moves += '<'*(-dx)
        return moves


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
            print('L1:', cur)
            continue
        for m in more[0]:
            q.append((cur + m, more[1:]))

    level_2_combs = []
    for level_1 in level_1_combs:
        dpad_1 = DirectionalKeypad()
        level_2 = []
        for c in level_1:
            level_2 += dpad_1.move_to(c)
            level_2 += 'A'
        level_2_combs.append(level_2)
        print('L2:', ''.join(level_2))

    level_3_combs = []
    for level_2 in level_2_combs:
        dpad_2 = DirectionalKeypad()
        level_3 = []
        for c in level_2:
            level_3 += dpad_2.move_to(c)
            level_3 += 'A'
        level_3_combs.append(level_3)
        print('L3:', ''.join(level_3))

    level_3 = sorted(level_3_combs, key=lambda c: len(c))[0]
    print('L3:', ''.join(level_3), '*', len(level_3))

    print('--- check ---')
    dpad_2.reset()
    dpad_1.reset()
    numpad.reset()

    print(' ', '  ', dpad_2.key, dpad_1.key, numpad.key)
    pressed = []
    for c in level_3:
        if c != 'A':
            dpad_2.move(c)
        else:
            if dpad_2.key != 'A':
                dpad_1.move(dpad_2.key)
            else:
                if dpad_1.key != 'A':
                    numpad.move(dpad_1.key)
                else:
                    pressed.append(numpad.key)
        print(c, '->', dpad_2.key, dpad_1.key, numpad.key, ''.join(pressed))
    if ''.join(pressed) != code:
        raise(BaseException(f'code mismatched in: {code}, out: {pressed}'))
    else:
        print('  ->', ''.join(pressed))
    score += len(level_3) * int(code[:-1])

print(score)
