#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of functions."""

import sieves
import os


def verbosity_level(args):
    """Check verbosity level."""
    verbosity = args.verbose
    if args.quiet is True:
        verbosity = -1
    return verbosity


def select_divisormethod(args):
    """Select specified divisor method."""
    if args.divisormethod == 'all':
        divisorfunc = sieves.isprime_all_break
    elif args.divisormethod == 'sqrt':
        divisorfunc = sieves.isprime_sqrt_break
    return divisorfunc


def select_algorithm(algorithm, divisorfunc, limit, hide_progress, verbosity):
    """Select specified algorithm."""
    if algorithm.sievemethod == 'all':
        primes = sieves.alg_all(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'odd':
        primes = sieves.alg_odd(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '6k':
        primes = sieves.alg_6k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '4k':
        primes = sieves.alg_4k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '3k':
        primes = sieves.alg_3k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'list':
        primes = sieves.alg_multiples_all(limit, hide_progress)
    elif algorithm.sievemethod == 'list-np':
        primes = sieves.alg_multiples_all_np(limit, hide_progress)
    elif algorithm.sievemethod == 'divisors':
        primes = sieves.numdivisors(limit, hide_progress)
    return primes


def auto_filename(args, verbosity):
    """Generate auto filename."""
    # If autoname option is not used, take outfile argument,
    # else generate auto filename
    if args.autoname is False:
        outfile = args.outfile
    else:
        filename = 'Eratosthenes_{}_{}_{}.dat'.format(args.limit,
                                                      args.sievemethod,
                                                      args.divisormethod)
        path = os.path.dirname(args.outfile)
        outfile = os.path.join(path, filename)
        if verbosity >= 1:
            print('[auto-name] Using option --auto-name')
            print('[auto-name] Composing output filename from '
                  'limit ({}), sieve method ({}), and divisor method '
                  '({}).'.format(args.limit, args.sievemethod,
                                 args.divisormethod))
            print('[auto-name] Generated auto filename: {}'.format(filename))
            print('[auto-name] Using path from positional argument outfile: '
                  '{}'.format(path))
    if verbosity >= 1:
        if args.outfile is None:
            print('[output] No output file specified. No file output.')
        else:
            print('[output] Writing output to: {}'.format(outfile))
    return outfile
