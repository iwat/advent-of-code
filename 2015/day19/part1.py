import pytest
import sys


@pytest.mark.parametrize('repl, molecule, expected', [
    ([('H', 'HO'), ('H', 'OH'), ('O', 'HH')], 'HOH', ['HOOH', 'OHOH', 'HOHO', 'HHHH']),
    ])
def test_solve(repl, molecule, expected):
    sol = solve(repl, molecule)
    assert sol == set(expected)


def solve(repl, molecule):
    generated = set()
    for before, after in repl:
        ndx = 0
        while True:
            try:
                loc = molecule.index(before, ndx)
                gen = molecule[0:loc] + after + molecule[loc+len(before):]
                generated.add(gen)
                ndx = loc + len(before)
            except ValueError:
                break
    return generated


def main():
    repl = [l.strip() for l in sys.stdin.readlines() if l.strip() != '']
    molecule = repl[-1]
    repl = repl[:-1]

    repl = [tuple(e.split(' => ')) for e in repl]

    result = solve(repl, molecule)
    print(len(result))


if __name__ == '__main__':
    main()
