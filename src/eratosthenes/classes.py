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


class Result(Algorithm):
    """Define result class."""

    def __init__(self, divisormethod, sievemethod, version, limit,
                 elapsed_time, progress_bar_active, primes):
        super().__init__(divisormethod, sievemethod)
        self.version = version
        self.limit = limit
        self.num_primes = len(primes)
        self.elapsed_time = elapsed_time
        self.progress_bar_active = progress_bar_active
        self.primes = primes
