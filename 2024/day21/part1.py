import sys


class NumericKeypad:
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

    def __init__(self):
        self.key = 'A'
        self.pos = self.KEY_TO_POS['A']

    def reset(self):
        self.key = 'A'
        self.pos = self.KEY_TO_POS['A']

    def move_to(self, k):
        if c == self.key:
            return []
        new_pos = self.KEY_TO_POS[k]
        dx, dy = new_pos[0] - self.pos[0], new_pos[1] - self.pos[1]
        self.pos = new_pos
        self.key = k

        moves = []
        if dy < 0:
            moves += '^'*(-dy)
        if dx > 0:
            moves += '>'*(dx)
        if dy > 0:
            moves += 'v'*(dy)
        if dx < 0:
            moves += '<'*(-dx)
        return moves

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
        self.key = self.POS_TO_KEY[self.pos]


class DirectionalKeypad:
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

    def __init__(self):
        self.key = 'A'
        self.pos = self.KEY_TO_POS['A']

    def reset(self):
        self.key = 'A'
        self.pos = self.KEY_TO_POS['A']

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
        self.key = self.POS_TO_KEY[self.pos]
        return self.key


score = 0
codes = [l.strip() for l in sys.stdin.readlines()]
for code in codes:
    print('---', code, '---')
    level_1 = []
    numpad = NumericKeypad()
    for c in list(code):
        level_1 += numpad.move_to(c)
        level_1 += 'A'
    print(''.join(level_1))

    level_2 = []
    dpad_1 = DirectionalKeypad()
    for c in level_1:
        level_2 += dpad_1.move_to(c)
        level_2 += 'A'
    print(''.join(level_2))

    level_3 = []
    dpad_2 = DirectionalKeypad()
    for c in level_2:
        level_3 += dpad_2.move_to(c)
        level_3 += 'A'
    print(''.join(level_3))

    if code == '379A':
        level_3 = list('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')

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
