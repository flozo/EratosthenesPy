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


def select_algorithm_memory_mode(divisor_method, sieve_method, settings,
                                 verbosity):
    """Select specified algorithm."""
    if settings.sievemethod == 'all':
        result_code = sieves.alg_all(divisor_method.function,
                                     settings.limit_specified,
                                     settings.progress_bar_active)
    elif settings.sievemethod == 'odd':
        result_code = sieves.alg_odd(divisor_method.function,
                                     settings.limit_specified,
                                     settings.progress_bar_active)
    elif settings.sievemethod in ('6k', '4k', '3k'):
        result_code = sieves.alg_fk(sieve_method,
                                    divisor_method.function,
                                    settings.limit_specified,
                                    settings.progress_bar_active)
    elif settings.sievemethod == 'list':
        result_code = sieves.alg_multiples_all(settings.limit_specified,
                                               settings.progress_bar_active)
    elif settings.sievemethod == 'list-np':
        result_code = sieves.alg_multiples_all_np(settings.limit_specified,
                                                  settings.progress_bar_active)
    elif settings.sievemethod == 'divisors':
        result_code = sieves.numdivisors(settings.limit_specified,
                                         settings.progress_bar_active)
    return result_code


def select_algorithm_storage_mode(divisor_method, sieve_method, settings,
                                  verbosity):
    """Select specified algorithm."""
    if settings.sievemethod == 'all':
        result_code = sv.alg_all(divisor_method.function,
                                 settings.limit_specified,
                                 settings.tempfile,
                                 settings.progress_bar_active)
    elif settings.sievemethod == 'odd':
        result_code = sv.alg_odd(divisor_method.function,
                                 settings.limit_specified,
                                 settings.tempfile,
                                 settings.progress_bar_active)
    elif settings.sievemethod in ('6k', '4k', '3k'):
        result_code = sv.alg_fk(sieve_method,
                                divisor_method.function,
                                settings.limit_specified,
                                settings.tempfile,
                                settings.progress_bar_active)
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
        else:
            print('[mode] Write directly to file.')
    if verbosity >= 1:
        if args.outfile is None:
            print('[output] No output file specified. No file output.')
        else:
            print('[output] Writing output to: \'{}\''.format(outfile))
    return outfile


def output(divisor_method, sieve_method, settings, result, verbosity):
    """Generate output file."""
    title = 'Eratosthenes v{}'.format(settings.version)
    header_width = len(title) // 3 * 5
    header_top = '# {0} {1} {0}\n'.format('═' * int(header_width // 3), title)
    header_closing = '# {}\n'.format('═' * (len(header_top) - 4))

    if sieve_method.name != 'divisors':
        header_settings = [
            ['Integer range', '[0, {}]'.format(settings.limit_specified)],
            ['Sieve method', sieve_method.name],
            ['Divisors method', divisor_method.name],
            ['Progress bar active', '{}'.format(settings.progress_bar_active)],
            ['On-the-fly writing mode', settings.mode]
            ]
        header_result = [
            ['Interrupt exception event', '{}'.format(result.interrupt)],
            ['Iterations completed',
             '{} of {} ({:6.2f}%)'.format(result.last_iter,
                                          settings.iterations,
                                          result.percentage_completed)],
            ['Actually tested integer range',
             '[0, {}]'.format(result.limit_actual)],
            ['Detected prime numbers', result.num_primes],
            ['Sifting time', '{:.9f} seconds'.format(result.elapsed_time)],
            ]
        if verbosity >= 0:
            print('[result] Detected {} prime numbers in {:.9f} '
                  'seconds.'.format(result.num_primes, result.elapsed_time))
        if settings.outfile is not None:
            with open(settings.outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                f.write('#   [Specified settings]\n')
                for item in header_settings:
                    f.write('#   {:<31} {:<31}\n'.format(item[0], item[1]))
                f.write('# {}\n'.format('─' * (len(header_top) - 4)))
                f.write('#   [Result summary]\n')
                for item in header_result:
                    f.write('#   {:<31} {:<31}\n'.format(item[0], item[1]))
                f.write(header_closing)
                for i in range(result.num_primes):
                    f.write('{}\n'.format(result.primes[i]))
    else:
        header = [
            ['Integer range', '[0, {}]'.format(settings.limit)],
            ['Applied divisors method', divisor_method.name],
            ['Progress bar active', '{}'.format(settings.progress_bar_active)],
            ['Time', '{:.9f} seconds'.format(result.elapsed_time)],
            ]
        if verbosity >= 0:
            print('Created divisor list in the rage [1, {}] in {:.9f} '
                  'seconds'.format(result.limit, result.elapsed_time))
        if settings.outfile is not None:
            with open(settings.outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                for item in header:
                    f.write('#  {:<31} {:<31}\n'.format(item[0], item[1]))
                f.write(header_closing)
                f.write('#  Number\tDivisors\n')
                for i in range(result.num_primes):
                    f.write('{}\t{}\n'.format(result.primes[i][0],
                                              result.primes[i][1]))
    if settings.mode == 'storage':
        # Check keep mode and treat temporary file as specified
        if verbosity >= 1:
            print('[keep] Keep mode: \'{}\'.'.format(settings.keep))
            print('[keep] Interrupt exception: \'{}\'.'.format(result.interrupt))
        if settings.keep == 'never' or (settings.keep == 'interrupt' and
                                        result.interrupt is False):
            os.remove(settings.tempfile)
            if verbosity >= 1:
                print('[keep] Temporary file \'{}\' '
                      'deleted.'.format(settings.tempfile))
        else:
            if verbosity >= 1:
                print('[keep] Keep temporary '
                      'file \'{}\'.'.format(settings.tempfile))
    # elif settings.mode == 'memory':
    #     if verbosity >= 1:
    #         print('')
