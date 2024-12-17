import time


def resolve(state, operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return state['A']
    if operand == 5:
        return state['B']
    if operand == 6:
        return state['C']
    raise(BaseException(f'unknown operand {operand}'))


def adv(state, operand):
    numerator = state['A']
    denominator = 2 ** resolve(state, operand)
    state['A'] = numerator // denominator
    state['PC'] += 2


def bxl(state, operand):
    state['B'] = state['B'] ^ operand
    state['PC'] += 2


def bst(state, operand):
    state['B'] = resolve(state, operand) % 8
    state['PC'] += 2


def jnz(state, operand):
    if state['A'] == 0:
        state['PC'] += 2
    else:
        state['PC'] = operand


def bxc(state, _operand):
    val1 = state['B']
    val2 = state['C']
    state['B'] = val1 ^ val2
    state['PC'] += 2


def out(state, operand):
    state['output'].append(resolve(state, operand) % 8)
    state['PC'] += 2


def bdv(state, operand):
    numerator = state['A']
    denominator = 2 ** resolve(state, operand)
    state['B'] = numerator // denominator
    state['PC'] += 2


def cdv(state, operand):
    numerator = state['A']
    denominator = 2 ** resolve(state, operand)
    state['C'] = numerator // denominator
    state['PC'] += 2


execute = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def run(state, instructions):
    state['PC'] = 0
    state['output'] = []
    print('       ', state)
    while state['PC'] < len(instructions):
        inst = instructions[state['PC']]
        operand = instructions[state['PC'] + 1]
        execute[inst](state, operand)
        print(inst, execute[inst].__name__, operand, state)
    print(','.join([str(o) for o in state['output']]))


print('--- 1 ---')
run({'A': 729, 'B': 0, 'C': 0}, [0, 1, 5, 4, 3, 0])
print()
print('--- 2 ---')
run({'A': 25986278, 'B': 0, 'C': 0}, [2, 4, 1, 4, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0])

