import collections
import random
import sys


def solve(repl, molecule):
    random.shuffle(repl)
    molecules = [molecule]
    steps = 0

    attempts = 0
    while molecule != 'e':
        updated = False
        for before, after in repl:
            new_molecule = molecule.replace(after, before, 1)
            if new_molecule == molecule:
                continue
            #print(new_molecule)
            steps += 1
            molecule = new_molecule
            updated = True
            molecules.append(molecule)
        if not updated:
            molecule = molecules[len(molecules)//2]
            repl = repl[1:]
            attempts += 1
        if attempts > 100:
            return None
    return steps


def main():
    repl = [l.strip() for l in sys.stdin.readlines() if l.strip() != '']
    molecule = repl[-1]
    repl = repl[:-1]

    repl = [tuple(e.split(' => ')) for e in repl]

    best_result = None
    for i in range(200):
        result = solve(repl, molecule)
        if result is not None:
            if best_result is None or best_result > result:
                best_result = result
    print(best_result)


if __name__ == '__main__':
    main()
