# Test functions for eratosthenes.sieves
# v0.1 2021-06-19

import eratosthenes.sieves as sv


def test_divisors_all():
    result12 = [1, 2, 3, 4, 6, 12]
    result1000 = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]
    result360 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360]
    assert sv.divisors_all(12) == result12
    assert sv.divisors_all(1000) == result1000
    assert sv.divisors_all(360) == result360


def test_divisors_sqrt():
    result12 = [1, 2, 3, 12]
    result1000 = [1, 2, 4, 5, 8, 10, 20, 25, 1000]
    result360 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 360]
    assert sv.divisors_sqrt(12) == result12
    assert sv.divisors_sqrt(1000) == result1000
    assert sv.divisors_sqrt(360) == result360


def test_isprime():
    primes = [2, 3, 5, 991429, 188748146801, 492366587,
                  7596952219, 32212254719]
    composites = [4, 6, 12, 360, 12345678902]
    other_nonprimes = [0, 1]
    for prime in primes:
        assert sv.isprime(prime) == True
    for composite in composites:
        assert sv.isprime(composite) == False
    for other_nonprime in other_nonprimes:
        assert sv.isprime(other_nonprime) == False


# Expected results (independent of sieve algorithm)
primesdict = {
    0: [],
    1: [],
    2: [2],
    3: [2, 3],
    4: [2, 3],
    5: [2, 3, 5],
    6: [2, 3, 5],
    7: [2, 3, 5, 7],
    8: [2, 3, 5, 7],
    9: [2, 3, 5, 7],
    10: [2, 3, 5, 7],
    11: [2, 3, 5, 7, 11],
    100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    }


# Sieve algorithms
def test_alg_all():
   for key in primesdict:
        assert sv.alg_all(sv.divisors_all, key) == primesdict[key]


def test_alg_odd():
   for key in primesdict:
        assert sv.alg_odd(sv.divisors_all, key) == primesdict[key]


def test_alg_6k():
   for key in primesdict:
        assert sv.alg_6k(sv.divisors_all, key) == primesdict[key]


def test_alg_4k():
   for key in primesdict:
        assert sv.alg_4k(sv.divisors_all, key) == primesdict[key]


def test_alg_3k():
   for key in primesdict:
        assert sv.alg_3k(sv.divisors_all, key) == primesdict[key]

