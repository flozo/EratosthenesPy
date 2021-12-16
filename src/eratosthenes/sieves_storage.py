#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of sieve algorithms for mode=storage."""


from tqdm import tqdm


def alg_all(divisorfunc, limit, outfile, hide_progress=False):
    """Check all numbers."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        for i in tqdm(range(2, limit+1), disable=hide_progress):
            if divisorfunc(i) is True:
                f.write('{}\n'.format(i))


def alg_odd(divisorfunc, limit, outfile, hide_progress=False):
    """Check only odd numbers."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 2)
        if limit >= 2:
            f.write('{}\n'.format(2))
        for i in tqdm(range(3, limit+1, 2), disable=hide_progress):
            if divisorfunc(i) is True:
                f.write('{}\n'.format(i))


def alg_fk(algorithm, divisorfunc, limit, outfile, hide_progress=False):
    """Check all numbers of form f*k+s_1 and f*k+s_2."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 3)
        if limit >= 2:
            f.write('{}\n'.format(2))
        if limit >= 3:
            f.write('{}\n'.format(3))
        end = (limit + algorithm.limit_shift) // algorithm.factor + 1
        for i in tqdm(range(1, end), disable=hide_progress):
            class1 = algorithm.factor * i + algorithm.summand1
            class2 = algorithm.factor * i + algorithm.summand2
            if divisorfunc(class1) is True:
                f.write('{}\n'.format(class1))
            # Check if class2 exceeds limit:
            if class2 <= limit and divisorfunc(class2) is True:
                f.write('{}\n'.format(class2))
