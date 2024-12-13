import re
import sys


class Gate:
    def __init__(self, output, input1 = None, input2 = None):
        self.resolved = None
        self.output = output
        if input1 is not None and input1.isnumeric():
            self.input1 = int(input1)
        else:
            self.input1 = input1
        if input2 is not None and input2.isnumeric():
            self.input2 = int(input2)
        else:
            self.input2 = input2

    def resolve(self):
        if not self.resolved:
            self.resolved = self._resolve()
        return self.resolved

    def set_resolved(self, resolved):
        self.resolved = resolved

    def reset(self):
        self.resolved = None

    def __repr__(self):
        return f'<- {self.input1} {type(self).__name__} {self.input2}'

class Assign(Gate):

    PATTERN = re.compile(r'^([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            return self.input1
        return self.input1.resolve()

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(2), m.group(1))

    def __repr__(self):
        return f'<- {self.input1}'

class AND(Gate):

    PATTERN = re.compile(r'^([0-9]+|[a-z]+) AND ([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            a = self.input1
        else:
            a = self.input1.resolve()
        if type(self.input2) == int:
            b = self.input2
        else:
            b = self.input2.resolve()
        return a & b

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(3), m.group(2), m.group(1))


class OR(Gate):

    PATTERN = re.compile(r'^([0-9]+|[a-z]+) OR ([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            a = self.input1
        else:
            a = self.input1.resolve()
        if type(self.input2) == int:
            b = self.input2
        else:
            b = self.input2.resolve()
        return a | b

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(3), m.group(2), m.group(1))


class LSHIFT(Gate):

    PATTERN = re.compile(r'^([0-9]+|[a-z]+) LSHIFT ([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            a = self.input1
        else:
            a = self.input1.resolve()
        if type(self.input2) == int:
            b = self.input2
        else:
            b = self.input2.resolve()
        return (a << b) & 0xffff

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(3), m.group(1), m.group(2))


class RSHIFT(Gate):

    PATTERN = re.compile(r'^([0-9]+|[a-z]+) RSHIFT ([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            a = self.input1
        else:
            a = self.input1.resolve()
        if type(self.input2) == int:
            b = self.input2
        else:
            b = self.input2.resolve()
        return a >> b

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(3), m.group(1), m.group(2))


class NOT(Gate):

    PATTERN = re.compile(r'^NOT ([0-9]+|[a-z]+) -> ([a-z]+)$')

    def _resolve(self):
        if type(self.input1) == int:
            a = self.input1
        else:
            a = self.input1.resolve()
        return ~a & 0xffff

    @classmethod
    def parse(cls, line):
        m = cls.PATTERN.match(line)
        if m is None:
            return None
        return cls(m.group(2), m.group(1))

    def __repr__(self):
        return f'<- NOT {self.input1}'


classes = [Assign, AND, OR, LSHIFT, RSHIFT, NOT]
registers = {}

for line in [l.strip() for l in sys.stdin.readlines()]:
    for c in classes:
        gate = c.parse(line)
        if gate is None:
            continue
        registers[gate.output] = gate


def wire(reg_name):
    reg = registers[reg_name]
    if isinstance(reg.input1, str):
        reg.input1 = wire(reg.input1)
    if isinstance(reg.input2, str):
        reg.input2 = wire(reg.input2)
    return reg


print(f'a:', wire('a').resolve())
old_a = wire('a').resolve()

for r in registers.values():
    r.reset()

wire('b').set_resolved(old_a)
print(f'a:', wire('a').resolve())
