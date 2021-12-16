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


def alg_6k(divisorfunc, limit, outfile, hide_progress=False):
    """Check all numbers of form 6k-1 and 6k+1."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 3)
        if limit >= 2:
            f.write('{}\n'.format(2))
        if limit >= 3:
            f.write('{}\n'.format(3))
        for i in tqdm(range(1, (limit+1)//6+1), disable=hide_progress):
            class1 = 6*i-1
            class2 = 6*i+1
            if divisorfunc(class1) is True:
                f.write('{}\n'.format(class1))
            # Check if class2 exceeds limit:
            if class2 <= limit and divisorfunc(class2) is True:
                f.write('{}\n'.format(class2))


def alg_4k(divisorfunc, limit, outfile, hide_progress=False):
    """Check all numbers of form 4k+1 and 4k+3."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 3)
        if limit >= 2:
            f.write('{}\n'.format(2))
        if limit >= 3:
            f.write('{}\n'.format(3))
        for i in tqdm(range(1, (limit-1)//4+1), disable=hide_progress):
            class1 = 4*i+1
            class2 = 4*i+3
            if divisorfunc(class1) is True:
                f.write('{}\n'.format(class1))
            # Check if class2 exceeds limit:
            if class2 <= limit and divisorfunc(class2) is True:
                f.write('{}\n'.format(class2))


def alg_3k(divisorfunc, limit, outfile, hide_progress=False):
    """Check all numbers of form 3k+1 and 3k+2."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 3)
        if limit >= 2:
            f.write('{}\n'.format(2))
        if limit >= 3:
            f.write('{}\n'.format(3))
        for i in tqdm(range(1, (limit-1)//3+1), disable=hide_progress):
            class1 = 3*i+1
            class2 = 3*i+2
            if divisorfunc(class1) is True:
                f.write('{}\n'.format(class1))
            # Check if class2 exceeds limit:
            if class2 <= limit and divisorfunc(class2) is True:
                f.write('{}\n'.format(class2))
