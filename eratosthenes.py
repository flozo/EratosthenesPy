#!/usr/bin/env python3
#
# Eratosthenes v0.4 2021-05-04

import argparse
import time
import numpy as np

# Define argument parsers and subparsers
parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. Written by Johannes Engelmayer')

parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.4 (2021-05-04)')
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='verbosity level (-v, -vv, -vvv): '
                    'default = single-line output, v = multi-line, vv = detailed, vvv = array output')
parser.add_argument('-q', '--quiet', action='store_true',
                    help=('disable terminal output (terminates all verbosity)'))
parser.add_argument('-m', '--method', dest='method', choices=('all', 'sqrt', 'odd-all', 'odd-sqrt'), default='sqrt', help='sieve method')
parser.add_argument('limit', type=int, default=100, help='upper limit of test range')
parser.add_argument('outfile', nargs='?', help='write to file')

args = parser.parse_args()
verbosity = args.verbose
if args.quiet is True:
    verbosity = -1

if verbosity >= 1:
    print(args)


def divisorsfasteven(number):
    divs = []
    divs.append(1)
    for i in range(2, int(np.sqrt(number))):
        if number % i == 0:
            divs.append(i)
    divs.append(number)
    return divs


def divisorsfast(number):
    divs = []
    divs.append(1)
    for i in range(2, int(np.sqrt(number))+1):
        if number % i == 0:
            divs.append(i)
    divs.append(number)
    return divs


def divisors(number):
    divs = []
    divs.append(1)
    for i in range(2, number):
        if number % i == 0:
            divs.append(i)
    divs.append(number)
    return divs


# check all numbers
def alg1(end):
    prime = []
    for i in range(2, end+1):
        if len(divisors(i)) == 2:
            prime.append(i)
    return prime


# check only to sqrt(n)
def alg2(end):
    prime = []
    for i in range(2, end+1):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime


# check only odd numbers
def alg3(end):
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisors(i)) == 2:
            prime.append(i)
    return prime


# check only odd numbers to sqrt(n)
def alg4(end):
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime

end = args.limit
method = args.method
outfile = args.outfile
start = time.process_time()
if method == 'all':
    primes = alg1(int(end))
elif method == 'sqrt':
    primes = alg2(int(end))
elif method == 'odd-all':
    primes = alg3(int(end))
elif method == 'odd-sqrt':
    primes = alg4(int(end))
else:
    if verbosity >= 0:
        print('Input invalid.')
if verbosity >= 0:
    print(primes)
elapsed = (time.process_time() - start)
if verbosity >= 0:
    print('Detected {} prime numbers in {:.5f} seconds.'.format(len(primes), elapsed))
if outfile is not None:
    with open(outfile, 'w', encoding='UTF-8') as f:
        f.write('# ********** Eratosthenes v0.4 2021-05-04 **********\n')
        f.write('# Tested integer range:   [2, {}]\n'.format(end))
        f.write('# Detected prime numbers: {}\n'.format(len(primes)))
        f.write('# Applied method:         {}\n'.format(method))
        f.write('# Sifting time:           {} seconds\n'.format(elapsed))
        f.write('# **************************************************\n')
        for i in range(len(primes)):
            f.write('{}\n'.format(primes[i]))

