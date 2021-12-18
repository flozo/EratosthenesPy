#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of functions."""

import sieves
import sieves_storage as sv
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


def select_algorithm_memory_mode(algorithm, divisorfunc, limit, hide_progress,
                                 verbosity):
    """Select specified algorithm."""
    if algorithm.sievemethod == 'all':
        primes = sieves.alg_all(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'odd':
        primes = sieves.alg_odd(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod in ('6k', '4k', '3k'):
        primes = sieves.alg_fk(algorithm, divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'list':
        primes = sieves.alg_multiples_all(limit, hide_progress)
    elif algorithm.sievemethod == 'list-np':
        primes = sieves.alg_multiples_all_np(limit, hide_progress)
    elif algorithm.sievemethod == 'divisors':
        primes = sieves.numdivisors(limit, hide_progress)
    return primes


def select_algorithm_storage_mode(algorithm, divisorfunc, limit, outfile,
                                  hide_progress, verbosity):
    """Select specified algorithm."""
    if algorithm.sievemethod == 'all':
        result_code = sv.alg_all(divisorfunc, limit, outfile, hide_progress)
    elif algorithm.sievemethod == 'odd':
        result_code = sv.alg_odd(divisorfunc, limit, outfile, hide_progress)
    elif algorithm.sievemethod in ('6k', '4k', '3k'):
        result_code = sv.alg_fk(algorithm, divisorfunc, limit, outfile,
                                hide_progress)
    return result_code


def auto_filename(args, verbosity):
    """Generate auto filename."""
    # If autoname option is not used, take outfile argument,
    # else generate auto filename
    if args.autoname is False:
        outfile = args.outfile
    else:
        filename = 'Eratosthenes_{}_{}_{}_{}.dat'.format(args.limit,
                                                         args.sievemethod,
                                                         args.divisormethod,
                                                         args.mode)
        path = os.path.dirname(args.outfile)
        outfile = os.path.join(path, filename)
        if verbosity >= 1:
            print('[auto-name] Composing output filename from '
                  'limit (\'{}\'), sieve method (\'{}\'), divisor '
                  'method (\'{}\'), and writing mode '
                  '(\'{}\').'.format(args.limit, args.sievemethod,
                                     args.divisormethod, args.mode))
            print('[auto-name] Generated auto filename: '
                  '\'{}\''.format(filename))
            print('[auto-name] Using path from positional argument outfile: '
                  '\'{}\''.format(path))
    if verbosity >= 1:
        print('[mode] On-the-fly writing mode is \'{}\'.'.format(args.mode))
        if args.mode == 'memory':
            print('[mode] First write to array; after completion write '
                  'to file.')
            print('[mode] Results are LOST upon interrupt!')
        else:
            print('[mode] Write directly to file.')
            print('[mode] Results are PRESERVED upon interrupt!')
            print('[mode] If aborted, results can be found in headerless '
                  'temporary file \'{}\'.'.format(outfile + '.temp'))
    if verbosity >= 1:
        if args.outfile is None:
            print('[output] No output file specified. No file output.')
        else:
            print('[output] Writing output to: \'{}\''.format(outfile))
    return outfile


def output(result, outfile, verbosity):
    """Generate output file."""
    title = 'Eratosthenes v{}'.format(result.version)
    header_width = len(title) // 3 * 5
    header_top = '#  {0} {1} {0}\n'.format('*' * int(header_width // 3), title)
    header_closing = '#  {}\n'.format('*' * (len(header_top) - 4))
    percentage = result.last_iter/result.iterations * 100

    if result.sievemethod != 'divisors':
        header = [
            ['Specified integer range', '[0, {}]'.format(result.limit)],
            ['Interrupt exception', '{}'.format(result.interrupt)],
            ['Iterations completed',
             '{} of {} ({:6.2f}%)'.format(result.last_iter,
                                          result.iterations,
                                          percentage)],
            ['Actually tested integer range',
             '[0, {}]'.format(result.actual_limit)],
            ['Detected prime numbers', result.num_primes],
            ['Applied sieve method', result.sievemethod],
            ['Applied divisors method', result.divisormethod],
            ['Progress bar active', result.progress_bar_active],
            ['On-the-fly writing mode', result.mode],
            ['Sifting time', '{:.9f} seconds'.format(result.elapsed_time)],
            ]
        if verbosity >= 0:
            print('[result] Detected {} prime numbers in {:.9f} '
                  'seconds.'.format(result.num_primes, result.elapsed_time))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                for item in header:
                    f.write('#  {:<31} {:<31}\n'.format(item[0], item[1]))
                f.write(header_closing)
                for i in range(result.num_primes):
                    f.write('{}\n'.format(result.primes[i]))
    else:
        header = [
            ['Integer range', '[0, {}]'.format(result.limit)],
            ['Applied divisors method', result.divisormethod],
            ['Progress bar active', result.progress_bar_active],
            ['Time', '{:.9f} seconds'.format(result.elapsed_time)],
            ]
        if verbosity >= 0:
            print('Created divisor list in the rage [1, {}] in {:.9f} '
                  'seconds'.format(result.limit, result.elapsed_time))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                for item in header:
                    f.write('#  {:<31} {:<31}\n'.format(item[0], item[1]))
                f.write(header_closing)
                f.write('#  Number\tDivisors\n')
                for i in range(result.num_primes):
                    f.write('{}\t{}\n'.format(result.primes[i][0],
                                              result.primes[i][1]))
    # Check keep mode and treat temporary file as specified
    if verbosity >= 1:
        print('[keep] Keep mode: \'{}\'.'.format(result.keep))
        print('[keep] Interrupt exception: \'{}\'.'.format(result.interrupt))
    if result.keep == 'never' or (result.keep == 'interrupt' and
                                  result.interrupt is False):
        os.remove(outfile + '.temp')
        if verbosity >= 1:
            print('[keep] Temporary file \'{}\' '
                  'deleted.'.format(outfile + '.temp'))
    else:
        if verbosity >= 1:
            print('[keep] Keep temporary '
                  'file \'{}\'.'.format(outfile + '.temp'))
