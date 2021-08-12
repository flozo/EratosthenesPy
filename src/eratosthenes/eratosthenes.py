#!/usr/bin/env python3
#

version_num = '0.12'
version_dat = '2021-08-12'
version_str = '{} ({})'.format(version_num, version_dat)

# Import modules

import argparse
import time
import numpy as np
import os
import sieves


def main():
    # Define argument parsers and subparsers
    parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. (https://github.com/flozo/Eratosthenes)')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s '+ version_str)
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='verbosity level (-v, -vv, -vvv): '
                        'default = single-line output, v = multi-line, vv = detailed, vvv = array output')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help=('disable terminal output (terminates all verbosity)'))
    parser.add_argument('-s', '--sievemethod', dest='sievemethod', choices=('all', 'odd', '3k', '4k', '6k', 'list'), default='6k', help='sieve method')
    parser.add_argument('-d', '--divisormethod', dest='divisormethod', choices=('all', 'sqrt'), default='sqrt', help='divisor method')
    parser.add_argument('-a', '--auto-name', dest='autoname', action='store_true', help='generate output filename automatically as Eratosthenes-<limit>-<sievemethod>-<divisormethod>.dat')
    parser.add_argument('limit', type=int, default=100, help='upper limit of test range (a non-negative integer 0, 1, 2, 3, ...)')
    parser.add_argument('outfile', nargs='?', help='write to file')

    args = parser.parse_args()


    # Check verbosity level

    verbosity = args.verbose
    if args.quiet is True:
        verbosity = -1
    if verbosity >= 1:
        print(args)


    # Process arguments

    limit = int(args.limit)
    algorithm = sieves.Algorithm(args.divisormethod, args.sievemethod)
    if args.divisormethod == 'all':
        divisorfunc = sieves.divisors_all
    elif args.divisormethod == 'sqrt':
        divisorfunc = sieves.divisors_sqrt


    # If autoname option is not used, take outfile argument, else generate auto filename
    if args.autoname == False:
        outfile = args.outfile
    else:
        filename = 'Eratosthenes-{}-{}-{}.dat'.format(limit, args.sievemethod, args.divisormethod)
        path = os.path.dirname(args.outfile)
        outfile = os.path.join(path, filename)
        if verbosity >= 1:
            print('[auto-name] Using option --auto-name')
            print('[auto-name] Composing output filename from limit ({}), sieve method ({}), and divisor method ({}).'.format(limit, args.sievemethod, args.divisormethod))
            print('[auto-name] Generated auto filename: {}'.format(filename))
            print('[auto-name] Using path from positional argument outfile: {}'.format(path))
    if verbosity >= 1:
        if args.outfile is None:
            print('[output] No output file specified. No file output.')
        else:
            print('[output] Writing output to: {}'.format(outfile))
    start = time.process_time()


    # Use specified algorithms
    if algorithm.sievemethod == 'all':
        primes = sieves.alg_all(divisorfunc, limit)
    elif algorithm.sievemethod=='odd':
        primes = sieves.alg_odd(divisorfunc, limit)
    elif algorithm.sievemethod == '6k':
        primes = sieves.alg_6k(divisorfunc, limit)
    elif algorithm.sievemethod == '4k':
        primes = sieves.alg_4k(divisorfunc, limit)
    elif algorithm.sievemethod == '3k':
        primes = sieves.alg_3k(divisorfunc, limit)
    elif algorithm.sievemethod == 'list':
        primes = sieves.alg_multiples_all(limit)
    #elif method == 'divisors':
    #    primes = sieves.numdivisors(limit)
    if verbosity >= 3:
        print(primes)
    elapsed = (time.process_time() - start)


    # Generate output

    if algorithm.sievemethod != 'divisors':
        if verbosity >= 0:
            print('[result] Detected {} prime numbers in {:.5f} seconds.'.format(len(primes), elapsed))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write('# ************ Eratosthenes v{} ************\n'.format(version_str))
                f.write('# Tested integer range:    [0, {}]\n'.format(limit))
                f.write('# Detected prime numbers:  {}\n'.format(len(primes)))
                f.write('# Applied sieve method:    {}\n'.format(algorithm.sievemethod))
                f.write('# Applied divisors method: {}\n'.format(algorithm.divisormethod))
                f.write('# Sifting time:            {} seconds\n'.format(elapsed))
                f.write('# ********************************************************\n')
                for i in range(len(primes)):
                    f.write('{}\n'.format(primes[i]))
    else:
        if verbosity >=0:
            print('Created divisor list in the rage [1, {}] in {:5f} seconds'.format(limit, elapsed))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write('# ********** Eratosthenes v{} **********\n'.format(version_str))
                f.write('# Integer range:           [0, {}]\n'.format(limit))
                f.write('# Applied divisors method: {}\n'.format(algorithm.divisormethod))
                f.write('# Time:                    {} seconds\n'.format(elapsed))
                f.write('# **************************************************\n')
                f.write('# Number\tDivisors\n')
                for i in range(len(primes)):
                    f.write('{}\t{}\n'.format(primes[i][0], primes[i][1]))

if __name__ == '__main__':
    main()

