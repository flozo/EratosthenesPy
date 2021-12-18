#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of classes."""


class Algorithm(object):
    """
    Define algorithm class with divisor method and sieve method.

    Divisor method can be: sqrt(default), all.
    Sieve method can be: all, 6k(default), 4k, 3k, odd.
    """

    def __init__(self, divisormethod='sqrt', sievemethod='6k'):
        self.divisormethod = divisormethod
        self.sievemethod = sievemethod
        if sievemethod == '6k':
            factor = 6
            summand1 = -1
            summand2 = 1
            limit_shift = 1
        elif sievemethod == '4k':
            factor = 4
            summand1 = 1
            summand2 = 3
            limit_shift = -1
        elif sievemethod == '3k':
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


class Result(Algorithm):
    """Define result class."""

    def __init__(self, divisormethod, sievemethod, version, limit, iterations,
                 last_iter, actual_limit, elapsed_time, progress_bar_active,
                 mode, interrupt, keep, primes):
        super().__init__(divisormethod, sievemethod)
        self.version = version
        self.limit = limit
        self.iterations = iterations
        self.last_iter = last_iter
        self.actual_limit = actual_limit
        self.num_primes = len(primes)
        self.elapsed_time = elapsed_time
        self.progress_bar_active = progress_bar_active
        self.mode = mode
        self.interrupt = interrupt
        self.keep = keep
        self.primes = primes
