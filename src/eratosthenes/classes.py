#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of classes."""


import sieves


class DivisorMethod(object):
    """Define divisor-method class."""

    def __init__(self, name='sqrt'):
        self.name = name
        if name == 'all':
            self.function = sieves.isprime_all_break
            self.description = 'For primality test of n, check each integer '
            'up to n for being a divisor.'
        elif name == 'sqrt':
            self.function = sieves.isprime_sqrt_break
            self.description = 'For primality test of n, check each integer '
            'up to square root of n for being a divisor.'
        # self.function = fn.select_divisormethod(name)

    def show_description(self):
        """Show description."""
        print(self.description)


class SieveMethod(object):
    """Define sieve-method class."""

    def __init__(self, name='6k'):
        self.name = name
        if name == '6k':
            factor = 6
            summand1 = -1
            summand2 = 1
            limit_shift = 1
        elif name == '4k':
            factor = 4
            summand1 = 1
            summand2 = 3
            limit_shift = -1
        elif name == '3k':
            factor = 3
            summand1 = 1
            summand2 = 2
            limit_shift = -1
        else:
            factor = 0
            summand1 = 0
            summand2 = 0
            limit_shift = 0
        self.factor = factor
        self.summand1 = summand1
        self.summand2 = summand2
        self.limit_shift = limit_shift
        if name in ('6k', '4k', '3k'):
            self.description = 'Check integer numbers of form '
            '{0}*k+{1} and {0}*k+{2} for primality.'.format(factor,
                                                            summand1,
                                                            summand2)
        elif name == 'odd':
            self.description = 'Check odd integer numbers (2*k+1) for '
            'primality.'
        elif name == 'all':
            self.description = 'Check all integer numbers for primality.'

    def show_description(self):
        """Show description."""
        print(self.description)

    def get_iterations(self, limit):
        """Calculate number of iterations."""
        print(limit)
        if self.name in ('6k', '4k', '3k'):
            self.iterations = (limit + self.limit_shift) // self.factor + 1
        elif self.name == 'all':
            self.iterations = limit + 1
        elif self.name == 'odd':
            self.iterations = limit + 1 // 2
        else:
            self.iterations = 0
        return self.iterations


class Settings(object):
    """Define settings class."""

    def __init__(self, divisormethod, sievemethod, version, limit_specified,
                 iterations, progress_bar_active, mode, keep, outfile,
                 temp_ext):
        self.divisormethod = divisormethod
        self.sievemethod = sievemethod
        self.version = version
        self.limit_specified = limit_specified
        self.iterations = iterations
        self.progress_bar_active = progress_bar_active
        self.mode = mode
        self.keep = keep
        self.outfile = outfile
        self.tempfile = outfile + temp_ext


class Result(object):
    """Define result class."""

    def __init__(self, last_iter, percentage_completed, limit_actual,
                 elapsed_time, interrupt, primes):
        self.last_iter = last_iter
        self.percentage_completed = percentage_completed
        self.limit_actual = limit_actual
        self.num_primes = len(primes)
        self.elapsed_time = elapsed_time
        self.interrupt = interrupt
        self.primes = primes
