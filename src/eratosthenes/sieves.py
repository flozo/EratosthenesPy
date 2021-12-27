#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of sieve algorithms (memory mode)."""

import numpy as np
from tqdm import tqdm


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


# Prime-check algorithms

def isprime_all(number):
    """Check if number has more than 2 divisors up to number."""
    if number < 2:                  # 0 and 1 are not prime
        return False
    if number >= 2:
        for i in range(2, number):
            if number % i == 0:     # check for divisor other than 1 or number
                return False
        return True


def isprime_odd(number):
    """Check if number has more than 2 odd divisors up to number."""
    if number < 2:                  # 0 and 1 are not prime
        return False
    if number % 2 == 0:             # check if 2 is divisor
        return False
    if number > 2:
        for i in range(3, number, 2):
            if number % i == 0:     # check for divisor other than 1 or number
                return False
        return True


def isprime_sqrt(number):
    """Check if number has more than 2 divisors up to square root of number."""
    if number < 2:                  # 0 and 1 are not prime
        return False
    if number >= 2:
        for i in range(2, int(np.sqrt(number))+1):
            if number % i == 0:     # check for divisor other than 1 or number
                return False
        return True


def isprime_sqrt_odd(number):
    """Check if number has more than 2 odd divisors up to square root of number."""
    if number < 2:                  # 0 and 1 are not prime
        return False
    if number % 2 == 0:             # check if 2 is divisor
        return False
    if number > 2:
        for i in range(3, int(np.sqrt(number))+1, 2):
            if number % i == 0:     # check for divisor other than 1 or number
                return False
        return True


# Sieve algorithms

def alg_all(divisorfunc, limit_specified, progress_bar_active=True):
    """Check all numbers."""
    # Initialize variables
    prime = []
    interrupt = False
    limit_actual = limit_specified
    end = limit_specified + 1
    # Additional try block for handling keyboard interrupt
    try:
        for i in tqdm(range(2, end), disable=not(progress_bar_active)):
            if divisorfunc(i) is True:
                prime.append(i)
    except KeyboardInterrupt:
        limit_actual = i
        print('[KeyboardInterrupt exception] Interrupt at iteration '
              ' {} of {} ({:6.2f}%).'.format(i, end, i / end * 100))
        print('[KeyboardInterrupt exception] Actually '
              'tested integer range is [0, '
              '{}].'.format(limit_actual))
        interrupt = True
    finally:
        return prime, interrupt, i + 1, limit_actual


def alg_odd(divisorfunc, limit_specified, progress_bar_active=True):
    """Check odd numbers only."""
    # Initialize variables
    prime = []
    interrupt = False
    limit_actual = limit_specified
    end = limit_specified + 1
    # Special treatment for small limits (<= 2)
    if limit_specified >= 2:
        prime.append(2)
    # Additional try block for handling keyboard interrupt
    try:
        for i in tqdm(range(3, end, 2), disable=not(progress_bar_active)):
            if divisorfunc(i) is True:
                prime.append(i)
    except KeyboardInterrupt:
        limit_actual = i // 2
        print('[KeyboardInterrupt exception] Interrupt at iteration '
              ' {} of {} ({:6.2f}%).'.format(i, end, i / end * 100))
        print('[KeyboardInterrupt exception] Actually '
              'tested integer range is [0, '
              '{}].'.format(limit_actual))
        interrupt = True
    finally:
        return prime, interrupt, i + 1, limit_actual


def alg_fk(sieve_method, divisorfunc, limit_specified,
           progress_bar_active=True):
    """Check all numbers of form f*k+s_1 and f*k+s_2."""
    # Initialize variables
    prime = []
    interrupt = False
    limit_actual = limit_specified
    end = (limit_specified + sieve_method.limit_shift) // sieve_method.factor + 1
    # Special treatment for small limits (<= 3)
    if limit_specified >= 2:
        prime.append(2)
    if limit_specified >= 3:
        prime.append(3)
    # Additional try block for handling keyboard interrupt
    try:
        for i in tqdm(range(1, end), disable=not(progress_bar_active)):
            class1 = sieve_method.factor * i + sieve_method.summand1
            class2 = sieve_method.factor * i + sieve_method.summand2
            if divisorfunc(class1) is True:
                prime.append(class1)
            # Check if class2 exceeds limit:
            if class2 <= limit_specified and divisorfunc(class2) is True:
                prime.append(class2)
    except KeyboardInterrupt:
        limit_actual = sieve_method.factor * (i - 1) - sieve_method.limit_shift
        print('[KeyboardInterrupt exception] Interrupt at iteration '
              ' {} of {} ({:6.2f}%).'.format(i, end, i / end * 100))
        print('[KeyboardInterrupt exception] Actually '
              'tested integer range is [0, '
              '{}].'.format(limit_actual))
        interrupt = True
    finally:
        return prime, interrupt, i + 1, limit_actual


def alg_multiples_all(limit_specified, progress_bar_active=True):
    """Classical sieve of Eratosthenes with deletion of multiples."""
    nums = list(range(limit_specified+1))
    for j in tqdm(range(2, limit_specified+1),
                  disable=not(progress_bar_active)):
        for i in range(0, limit_specified+1):
            if nums[i] in nums[::j][2:]:
                nums[i] = 0             # Mark multiples of j as 0
    del nums[0]                         # Delete 0
    del nums[0]                         # Delete 1
    nums = [i for i in nums if i != 0]  # Delete all multiples marked as 0
    return nums


def alg_multiples_all_np(limit_specified, progress_bar_active=True):
    """Classical sieve of Eratosthenes with deletion of multiples (Numpy version)."""
    nums = np.arange(2, limit_specified+1)
    for j in tqdm(range(2, limit_specified+1),
                  disable=not(progress_bar_active)):
        multiples = np.arange(j, limit_specified+1, j)
        for i in multiples[1:]:
            nums = np.delete(nums, np.argwhere(nums == i))
    return nums


def numdivisors(end, progress_bar_active=True):
    """Determine the number of divisors of a number."""
    dividends = np.arange(start=1, stop=end+1, dtype=int)
    divisors = np.arange(start=1, stop=end+1, dtype=int)
    for i in tqdm(range(1, len(dividends)+1), disable=not(progress_bar_active)):
        ndivisors = 0
        for j in range(1, i//2+1):      # only check up to half
            if i % j == 0:
                ndivisors += 1
        divisors[i-1] = ndivisors+1     # add 1 for dividend itself
    new = np.column_stack([dividends, divisors])
    return new
