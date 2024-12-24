import sys


def calc(regs, wire, reg, level):
    if reg in regs:
        return
    reg1, op, reg2 = wire[reg]
    if reg1 not in regs:
        calc(regs, wire, reg1, level - 1)
    if reg2 not in regs:
        calc(regs, wire, reg2, level - 1)

    if op == 'AND':
        regs[reg] = regs[reg1] & regs[reg2]
    elif op == 'OR':
        regs[reg] = regs[reg1] | regs[reg2]
    elif op == 'XOR':
        regs[reg] = regs[reg1] ^ regs[reg2]
    else:
        raise(BaseException('unsupported op ' + op))
    print(' '*level, reg1, regs[reg1], op, reg2, regs[reg2], '->', reg, regs[reg])


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
    for ndx, zreg in enumerate(zregs[:-1]):
        print('---', zreg, '---')

        print('0 + 0 = 0')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        regs[zreg.replace('z', 'x')] = 0
        regs[zreg.replace('z', 'y')] = 0
        calc(regs, wire, zreg, ndx)
        assert regs[zreg] == 0

        print('1 + 0 = 1')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        regs[zreg.replace('z', 'x')] = 1
        regs[zreg.replace('z', 'y')] = 0
        calc(regs, wire, zreg, ndx)
        assert regs[zreg] == 1

        print('0 + 1 = 1')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        regs[zreg.replace('z', 'x')] = 0
        regs[zreg.replace('z', 'y')] = 1
        calc(regs, wire, zreg, ndx)
        assert regs[zreg] == 1

        print('1 + 1 = 0 (+1)')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        regs[zreg.replace('z', 'x')] = 1
        regs[zreg.replace('z', 'y')] = 1
        calc(regs, wire, zreg, ndx)
        assert regs[zreg] == 0

        print('0 + 0 (+1) = 1')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        if ndx > 0:
            prev_z = zregs[ndx - 1]
            regs[prev_z.replace('z', 'x')] = 1
            regs[prev_z.replace('z', 'y')] = 1
            regs[zreg.replace('z', 'x')] = 0
            regs[zreg.replace('z', 'y')] = 0
            calc(regs, wire, zreg, ndx)
            assert regs[zreg] == 1

        print('1 + 0 (+1) = 0 (+1)')
        regs = {}
        for prev in range(ndx):
            prev_z = zregs[prev]
            regs[prev_z.replace('z', 'x')] = 0
            regs[prev_z.replace('z', 'y')] = 0
        if ndx > 0:
            prev_z = zregs[ndx - 1]
            regs[prev_z.replace('z', 'x')] = 1
            regs[prev_z.replace('z', 'y')] = 1
            regs[zreg.replace('z', 'x')] = 1
            regs[zreg.replace('z', 'y')] = 0
            calc(regs, wire, zreg, ndx)
            assert regs[zreg] == 0




if __name__ == '__main__':
    main()


# For the full adder of zN, we expect in order (where order of args doesnt matter):
# zN <- a XOR b
#   a  <- xN XOR yN
#   b  <- c OR d
#      c <- xN-1 AND yN-1
#      d <- e AND f
#        e <- xN-1 XOR yN-1
#        f <- g OR h
#        ... repeats until z00
#
# z07 - shj
# wkb - tpk
# z23 - pfn
# z27 - kcd
#
# kcd
# pfn
# shj
# tpk
# wkb
# z07
# z23
# z27
