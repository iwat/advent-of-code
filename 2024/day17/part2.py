import datetime


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
    denumerator = 2 ** resolve(state, operand)
    state['A'] = numerator // denumerator
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
    denumerator = 2 ** resolve(state, operand)
    state['B'] = numerator // denumerator
    state['PC'] += 2


def cdv(state, operand):
    numerator = state['A']
    denumerator = 2 ** resolve(state, operand)
    state['C'] = numerator // denumerator
    state['PC'] += 2


execute = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def run(state, instructions, min_a, max_a):
    start = datetime.datetime.now()
    suffixes = []
    current_suffix = None
    current_suffix_start = None

    suffix_size = 14
    instruction_suffix = instructions[-suffix_size:]

    for initial_a in range(min_a, max_a, 1):
        state['PC'] = 0
        state['A'] = initial_a
        state['output'] = []
        #print('       ', state)
        while state['PC'] < len(instructions):
            inst = instructions[state['PC']]
            operand = instructions[state['PC'] + 1]
            execute[inst](state, operand)

        if len(state['output']) > len(instructions):
            break
        if len(state['output']) < len(instructions):
            continue

        suffix = state['output'][-suffix_size:]

        if current_suffix != suffix:
            if current_suffix is not None and current_suffix == instruction_suffix:
                print((current_suffix_start, initial_a - 1, current_suffix))
                suffixes.append((current_suffix_start, initial_a - 1, current_suffix))
            current_suffix = suffix
            current_suffix_start = initial_a

        if state['output'] == instructions:
            print(initial_a, state['output'])
            break


print('--- 2 ---')
run(
        {'A': 25986278, 'B': 0, 'C': 0},
        [2, 4, 1, 4, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0],
        156985331105412,
        157985331105672,
        )
