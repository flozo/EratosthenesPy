#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test functions for eratosthenes.sieves."""

import eratosthenes.sieves as sv
from eratosthenes.classes import SieveMethod as sm


def test_divisors_all():
    result12 = [1, 2, 3, 4, 6, 12]
    result1000 = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500,
                  1000]
    result360 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40,
                 45, 60, 72, 90, 120, 180, 360]
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


def test_isprime_all():
    primes = [2, 3, 5, 991429]
    composites = [4, 6, 12, 360, 12345678902]
    other_nonprimes = [0, 1]
    for prime in primes:
        assert sv.isprime_all(prime) is True
    for composite in composites:
        assert sv.isprime_all(composite) is False
    for other_nonprime in other_nonprimes:
        assert sv.isprime_all(other_nonprime) is False


def test_isprime_odd():
    primes = [2, 3, 5, 991429]
    composites = [4, 6, 12, 360, 12345678902]
    other_nonprimes = [0, 1]
    for prime in primes:
        assert sv.isprime_odd(prime) is True
    for composite in composites:
        assert sv.isprime_odd(composite) is False
    for other_nonprime in other_nonprimes:
        assert sv.isprime_odd(other_nonprime) is False


def test_isprime_sqrt():
    primes = [2, 3, 5, 991429, 188748146801, 492366587, 7596952219,
              32212254719]
    composites = [4, 6, 12, 360, 12345678902]
    other_nonprimes = [0, 1]
    for prime in primes:
        assert sv.isprime_sqrt(prime) is True
    for composite in composites:
        assert sv.isprime_sqrt(composite) is False
    for other_nonprime in other_nonprimes:
        assert sv.isprime_sqrt(other_nonprime) is False


def test_isprime_sqrt_odd():
    primes = [2, 3, 5, 991429, 188748146801, 492366587, 7596952219,
              32212254719]
    composites = [4, 6, 12, 360, 12345678902]
    other_nonprimes = [0, 1]
    for prime in primes:
        assert sv.isprime_sqrt_odd(prime) is True
    for composite in composites:
        assert sv.isprime_sqrt_odd(composite) is False
    for other_nonprime in other_nonprimes:
        assert sv.isprime_sqrt_odd(other_nonprime) is False


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
    100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97]
    }


# Sieve algorithms
def test_alg_all():
    for key in primesdict:
        assert sv.alg_all(sv.isprime_all, key, False)[0] == primesdict[key]


def test_alg_odd():
    for key in primesdict:
        assert sv.alg_odd(sv.isprime_all, key, False)[0] == primesdict[key]


def test_alg_fk():
    for key in primesdict:
        assert sv.alg_fk(sm('6k'), sv.isprime_all,
                         key, False)[0] == primesdict[key]
    for key in primesdict:
        assert sv.alg_fk(sm('4k'), sv.isprime_all,
                         key, False)[0] == primesdict[key]
    for key in primesdict:
        assert sv.alg_fk(sm('3k'), sv.isprime_all,
                         key, False)[0] == primesdict[key]
