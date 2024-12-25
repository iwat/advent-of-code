import itertools
import pytest

primes = []

def gen_primes(max_val):
    if len(primes) > 0:
        min_val = primes[-1] + 1
    else:
        min_val = 2

    for v in range(min_val, max_val + 1):
        not_prime = any([v % p == 0 for p in primes])
        if not not_prime:
            primes.append(v)


def factorize(number):
    gen_primes(int(number ** 0.5) + 1)
    prime_factors = [p for p in primes if number % p == 0]

    numerator = number
    factors = []
    for p in prime_factors:
        while numerator % p == 0:
            numerator //= p
            factors.append(p)
    if numerator != 1:
        factors.append(numerator)

    assert mul(factors) == number

    return factors


@pytest.mark.parametrize('number, expected', [
    (2, [2]),
    (6, [2, 3]),
    (12, [2, 2, 3]),
    (60, [2, 2, 3, 5]),
    (93187, [93187]),
    ])
def test_factorize(number, expected):
    assert expected == factorize(number)


def mul(nums):
    result = 1
    for n in nums:
        result *= n
    return result


def solve(house_no, debug=False):
    if debug:
        print('-----', house_no, '-----')

    factors = factorize(house_no)
    if debug:
        print('f:', factors)
    elfs = set([(f,) for f in factors])
    for n in range(2, len(factors)):
        elfs.update(set(itertools.combinations(factors, n)))
    elfs = sorted([mul(nums) for nums in elfs])
    if house_no not in elfs:
        elfs.append(house_no)
    if debug:
        print('e:', elfs)

    presents = 1 * 10
    if debug:
        print('elf:', 1, '*', 10, '=', presents)
    for e in elfs:
        presents += e * 10
        if debug:
            print('elf:', '+', e, '*', 10, '=', e * 10, '==', presents)
    return presents


if __name__ == '__main__':
    GOAL = 33100000

    print('=====')
    highest_so_far = 0
    for i in range(1, GOAL // 10):
        presents = solve(i)
        if presents > highest_so_far:
            highest_so_far = presents
            print('sol:', f'{i:8d}', f'{presents:9d}', f'{highest_so_far:9d}')
            if presents >= GOAL:
                print('BINGO:', i, presents)
                solve(i, True)
                break
