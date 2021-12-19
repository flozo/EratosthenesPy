#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of sieve algorithms (storage mode)."""


from tqdm import tqdm


def alg_all(divisorfunc, limit_specified, outfile, progress_bar_active=True):
    """Check all numbers."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        for i in tqdm(range(2, limit_specified+1),
                      disable=not(progress_bar_active)):
            if divisorfunc(i) is True:
                f.write('{}\n'.format(i))


def alg_odd(divisorfunc, limit_specified, outfile, progress_bar_active=True):
    """Check only odd numbers."""
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 2)
        if limit_specified >= 2:
            f.write('{}\n'.format(2))
        for i in tqdm(range(3, limit_specified+1, 2),
                      disable=not(progress_bar_active)):
            if divisorfunc(i) is True:
                f.write('{}\n'.format(i))


def alg_fk(sieve_method, divisorfunc, limit_specified, outfile,
           progress_bar_active=True):
    """Check all numbers of form f*k+s_1 and f*k+s_2."""
    interrupt = False
    limit_actual = limit_specified
    with open(outfile, 'w', encoding='UTF-8') as f:
        # Special treatment for small limits (<= 3)
        if limit_specified >= 2:
            f.write('{}\n'.format(2))
        if limit_specified >= 3:
            f.write('{}\n'.format(3))
        end = (limit_specified + sieve_method.limit_shift) // sieve_method.factor + 1
        try:
            for i in tqdm(range(1, end), disable=not(progress_bar_active)):
                class1 = sieve_method.factor * i + sieve_method.summand1
                class2 = sieve_method.factor * i + sieve_method.summand2
                if divisorfunc(class1) is True:
                    f.write('{}\n'.format(class1))
                # Check if class2 exceeds limit:
                if class2 <= limit_specified and divisorfunc(class2) is True:
                    f.write('{}\n'.format(class2))
        except KeyboardInterrupt:
            limit_actual = sieve_method.factor * (i - 1) - sieve_method.limit_shift
            print('[KeyboardInterrupt exception] Interrupt at iteration '
                  ' {}.'.format(i))
            print('[KeyboardInterrupt exception] Actually '
                  'tested integer range is [0, '
                  '{}].'.format(limit_actual))
            interrupt = True
        finally:
            return interrupt, i + 1, limit_actual
