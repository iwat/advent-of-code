import sys


def calc(regs, wire, reg):
    if reg in regs:
        return
    reg1, op, reg2 = wire[reg]
    if reg1 not in regs:
        calc(regs, wire, reg1)
    if reg2 not in regs:
        calc(regs, wire, reg2)

    if op == 'AND':
        regs[reg] = regs[reg1] & regs[reg2]
    elif op == 'OR':
        regs[reg] = regs[reg1] | regs[reg2]
    elif op == 'XOR':
        regs[reg] = regs[reg1] ^ regs[reg2]
    else:
        raise(BaseException('unsupported op ' + op))
    print(reg1, regs[reg1], op, reg2, regs[reg2], '->', reg, regs[reg])


def main():
    regs = {}
    wire = {}
    while line := sys.stdin.readline().strip():
        if line == '':
            break
        reg, init = line.split(': ')
        regs[reg] = int(init)

    for line in [l.strip() for l in sys.stdin.readlines()]:
        ops, out = line.split(' -> ')
        reg1, op, reg2 = ops.split(' ')
        wire[out] = (reg1, op, reg2)

    zregs = sorted([k for k in wire.keys() if k[0] == 'z'])
    for zreg in zregs:
        calc(regs, wire, zreg)
    lsb = ''.join([str(regs[zreg]) for zreg in reversed(zregs)])
    print(int(lsb, 2))



if __name__ == '__main__':
    main()
