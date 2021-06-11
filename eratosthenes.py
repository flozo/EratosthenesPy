#!/usr/bin/env python3
#
# Eratosthenes v0.8 2021-06-11

# Version

version_num = '0.8'
version_dat = '2021-06-11'
version_str = '{} ({})'.format(version_num, version_dat)

# Import modules

import argparse
import time
import numpy as np
import sieves

# Define argument parsers and subparsers

parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. Written by Johannes Engelmayer')

parser.add_argument('-V', '--version', action='version', version='%(prog)s '+ version_str)
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='verbosity level (-v, -vv, -vvv): '
                    'default = single-line output, v = multi-line, vv = detailed, vvv = array output')
parser.add_argument('-q', '--quiet', action='store_true',
                    help=('disable terminal output (terminates all verbosity)'))
parser.add_argument('-d', '--divisormethod', dest='divisormethod', choices=('all', 'sqrt'), default='sqrt', help='divisor method')
parser.add_argument('-s', '--sievemethod', dest='sievemethod', choices=('all', 'odd', '3k', '4k', '6k'), default='6k', help='sieve method')
parser.add_argument('limit', type=int, default=100, help='upper limit of test range')
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
outfile = args.outfile
start = time.process_time()


# Use specified algorithms

if algorithm.sievemethod == 'all' and algorithm.divisormethod == 'all':
    primes = sieves.alg1(limit)
elif algorithm.sievemethod == 'all' and algorithm.divisormethod == 'sqrt':
    primes = sieves.alg2(limit)
elif algorithm.sievemethod == 'odd' and algorithm.divisormethod == 'all':
    primes = sieves.alg3(limit)
elif algorithm.sievemethod == 'odd' and algorithm.divisormethod == 'sqrt':
    primes = sieves.alg4(limit)
elif algorithm.sievemethod == '6k' and algorithm.divisormethod == 'all':
    primes = sieves.alg5(limit)
elif algorithm.sievemethod == '6k' and algorithm.divisormethod == 'sqrt':
    primes = sieves.alg6(limit)
elif algorithm.sievemethod == '4k' and algorithm.divisormethod == 'all':
    primes = sieves.alg7(limit)
elif algorithm.sievemethod == '4k' and algorithm.divisormethod == 'sqrt':
    primes = sieves.alg8(limit)
elif algorithm.sievemethod == '3k' and algorithm.divisormethod == 'all':
    primes = sieves.alg9(limit)
elif algorithm.sievemethod == '3k' and algorithm.divisormethod == 'sqrt':
    primes = sieves.alg10(limit)
#elif method == 'divisors':
#    primes = sieves.numdivisors(limit)
else:
    if verbosity >= 0:
        print('Input invalid.')
if verbosity >= 1:
    print(primes)
elapsed = (time.process_time() - start)


# Generate output

if algorithm.sievemethod != 'divisors':
    if verbosity >= 0:
        print('Detected {} prime numbers in {:.5f} seconds.'.format(len(primes), elapsed))
    if outfile is not None:
        with open(outfile, 'w', encoding='UTF-8') as f:
            f.write('# ************ Eratosthenes v{} ************\n'.format(version_str))
            f.write('# Tested integer range:    [2, {}]\n'.format(limit))
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
            f.write('# Integer range:           [2, {}]\n'.format(limit))
            f.write('# Applied divisors method: {}\n'.format(algorithm.divisormethod))
            f.write('# Time:                    {} seconds\n'.format(elapsed))
            f.write('# **************************************************\n')
            f.write('# Number\tDivisors\n')
            for i in range(len(primes)):
                f.write('{}\t{}\n'.format(primes[i][0], primes[i][1]))

