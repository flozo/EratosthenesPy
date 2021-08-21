#!/usr/bin/env python3
"""Collection of sieve algorithms."""

import numpy as np
from tqdm import tqdm


class Algorithm(object):
    """
    Define algorithm class with divisor method and sieve method.

    Divisor method can be: sqrt(default), all.
    Sieve method can be: all, 6k(default), 4k, 3k, odd.
    """

    def __init__(self, divisormethod='sqrt', sievemethod='6k'):
        self.divisormethod = divisormethod
        self.sievemethod = sievemethod


# Divisor algorithms

def divisors_all(number):
    """Determine divisors of number up to number."""
    divs = []
    if number < 1:              # 0 has no divisors
        return divs
    elif number >= 1:           # 1 is always divisor for number >= 1
        divs.append(1)
    if number >= 2:
        for i in range(2, number):
            if number % i == 0:
                divs.append(i)
        divs.append(number)     # number itself is always divisor
    return divs


def divisors_sqrt(number):
    """Determine all divisors of number up to square root of number."""
    divs = []
    if number < 1:              # 0 has no divisors
        return divs
    elif number >= 1:           # 1 is always divisor for number >= 1
        divs.append(1)
    if number >= 2:
        for i in range(2, int(np.sqrt(number))+1):
            if number % i == 0:
                divs.append(i)
        divs.append(number)     # number itself is always divisor
    return divs


def isprime(number):
    """Check if number is prime."""
    if len(divisors_sqrt(number)) == 2:
        return True
    else:
        return False


# Sieve algorithms

def alg_all(divisorfunc, limit, hide_progress=False):
    """Check all numbers."""
    prime = []
    for i in tqdm(range(2, limit+1), disable=hide_progress):
        if len(divisorfunc(i)) == 2:
            prime.append(i)
    return prime


def alg_odd(divisorfunc, limit, hide_progress=False):
    """Check only odd numbers."""
    prime = []
    # Special treatment of small limits (<= 2)
    if limit >= 2:
        prime.append(2)
    for i in tqdm(range(3, limit+1, 2), disable=hide_progress):
        if len(divisorfunc(i)) == 2:
            prime.append(i)
    return prime


def alg_6k(divisorfunc, limit, hide_progress=False):
    """Check all numbers of form 6k-1 and 6k+1."""
    prime = []
    # Special treatment of small limits (<= 3)
    if limit >= 2:
        prime.append(2)
    if limit >= 3:
        prime.append(3)
    for i in tqdm(range(1, (limit+1)//6+1), disable=hide_progress):
        class1 = 6*i-1
        class2 = 6*i+1
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        # Check if class2 exceeds limit:
        if class2 <= limit and len(divisorfunc(class2)) == 2:
            prime.append(class2)
        # progbar.update(1)
    return prime


def alg_4k(divisorfunc, limit, hide_progress=False):
    """Check all numbers of form 4k+1 and 4k+3."""
    prime = []
    # Special treatment of small limits (<= 3)
    if limit >= 2:
        prime.append(2)
    if limit >= 3:
        prime.append(3)
    for i in tqdm(range(1, (limit-1)//4+1), disable=hide_progress):
        class1 = 4*i+1
        class2 = 4*i+3
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        # Check if class2 exceeds limit:
        if class2 <= limit and len(divisorfunc(class2)) == 2:
            prime.append(class2)
    return prime


def alg_3k(divisorfunc, limit, hide_progress=False):
    """Check all numbers of form 3k+1 and 3k+2."""
    prime = []
    # Special treatment of small limits (<= 3)
    if limit >= 2:
        prime.append(2)
    if limit >= 3:
        prime.append(3)
    for i in tqdm(range(1, (limit-1)//3+1), disable=hide_progress):
        class1 = 3*i+1
        class2 = 3*i+2
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        # Check if class2 exceeds limit:
        if class2 <= limit and len(divisorfunc(class2)) == 2:
            prime.append(class2)
    return prime


def alg_multiples_all(limit, hide_progress=False):
    """Classical sieve of Eratosthenes with deletion of multiples."""
    nums = list(range(limit+1))
    for j in tqdm(range(2, limit+1), disable=hide_progress):
        for i in range(0, limit+1):
            if nums[i] in nums[::j][2:]:
                nums[i] = 0             # Mark multiples of j as 0
    del nums[0]                         # Delete 0
    del nums[0]                         # Delete 1
    nums = [i for i in nums if i != 0]  # Delete all multiples marked as 0
    return nums


def alg_multiples_all_np(limit, hide_progress=False):
    """Classical sieve of Eratosthenes with deletion of multiples. Numpy version."""
    nums = np.arange(2, limit+1)
    for j in tqdm(range(2, limit+1), disable=hide_progress):
        multiples = np.arange(j, limit+1, j)
        for i in multiples[1:]:
            nums = np.delete(nums, np.argwhere(nums == i))
    return nums


def numdivisors(end, hide_progress=False):
    """Determine the number of divisors of a number."""
    dividends = np.arange(start=1, stop=end+1, dtype=int)
    divisors = np.arange(start=1, stop=end+1, dtype=int)
    for i in tqdm(range(1, len(dividends)+1), disable=hide_progress):
        ndivisors = 0
        for j in range(1, i//2+1):      # only check up to half
            if i % j == 0:
                ndivisors += 1
        divisors[i-1] = ndivisors+1     # add 1 for dividend itself
    new = np.column_stack([dividends, divisors])
    return new
