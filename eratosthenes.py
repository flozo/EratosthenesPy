#!/usr/bin/env python3
#
# Eratosthenes v0.7 2021-05-06

# Version

version_num = '0.7'
version_dat = '2021-05-06'
version_str = '{} ({})'.format(version_num, version_dat)

# Import modules

import argparse
import time
import numpy as np

# Define argument parsers and subparsers

parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. Written by Johannes Engelmayer')

parser.add_argument('-V', '--version', action='version', version='%(prog)s '+ version_str)
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='verbosity level (-v, -vv, -vvv): '
                    'default = single-line output, v = multi-line, vv = detailed, vvv = array output')
parser.add_argument('-q', '--quiet', action='store_true',
                    help=('disable terminal output (terminates all verbosity)'))
parser.add_argument('-m', '--method', dest='method', choices=('all', 'sqrt', 'odd-all', 'odd-sqrt', '6k-all', '6k-sqrt', '4k-all', '4k-sqrt', '3k-all', '3k-sqrt', 'divisors'), default='sqrt', help='sieve method')
parser.add_argument('limit', type=int, default=100, help='upper limit of test range')
parser.add_argument('outfile', nargs='?', help='write to file')

args = parser.parse_args()

# Check verbosity level

verbosity = args.verbose
if args.quiet is True:
    verbosity = -1
if verbosity >= 1:
    print(args)


# Determine divisors of a number

def divisorsfast(number):
    """
    Determine all divisors of number up to square root of number
    """
    divs = []
    divs.append(1)
    for i in range(2, int(np.sqrt(number))+1):
        if number % i == 0:
            divs.append(i)
    divs.append(number)
    return divs


def divisors(number):
    """
    Determine all divisors of number up to number
    """
    divs = []
    divs.append(1)
    for i in range(2, number):
        if number % i == 0:
            divs.append(i)
    divs.append(number)
    return divs


# Sieve algorithms

def alg1(end):
    """
    Check all numbers up to upper endpoint
    """
    prime = []
    for i in range(2, end+1):
        if len(divisors(i)) == 2:
            prime.append(i)
    return prime


def alg2(end):
    """
    Check all numbers up to square root of upper endpoint
    """
    prime = []
    for i in range(2, end+1):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime


def alg3(end):
    """
    Check only odd numbers up to upper endpoint
    """
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisors(i)) == 2:
            prime.append(i)
    return prime


def alg4(end):
    """
    Check only odd numbers up to square root of upper endpoint
    """
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime

def alg5(end):
    """
    Check all numbers of form 6k-1 and 6k+1 up to upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-1)//6+1):
        class1 = 6*i-1
        class2 = 6*i+1
        if len(divisors(class1)) == 2:
            prime.append(class1)
        if len(divisors(class2)) == 2:
            prime.append(class2)
    return prime


def alg6(end):
    """
    Check all numbers of form 6k-1 and 6k+1 up to square root of upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-1)//6+1):
        class1 = 6*i-1
        class2 = 6*i+1
        if len(divisorsfast(class1)) == 2:
            prime.append(class1)
        if len(divisorsfast(class2)) == 2:
            prime.append(class2)
        if i % 1000 == 0:
            print('.', end='', flush=True)
    print('')
    return prime


def alg7(end):
    """
    Check all numbers of form 4k+1 and 4k+3 up to upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-3)//4+1):
        class1 = 4*i+1
        class2 = 4*i+3
        if len(divisors(class1)) == 2:
            prime.append(class1)
        if len(divisors(class2)) == 2:
            prime.append(class2)
    return prime


def alg8(end):
    """
    Check all numbers of form 4k+1 and 4k+3 up to square root of upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-3)//4+1):
        class1 = 4*i+1
        class2 = 4*i+3
        if len(divisorsfast(class1)) == 2:
            prime.append(class1)
        if len(divisorsfast(class2)) == 2:
            prime.append(class2)
    return prime


def alg9(end):
    """
    Check all numbers of form 3k+1 and 3k+2 up to upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-2)//3+1):
        class1 = 3*i+1
        class2 = 3*i+2
        if len(divisors(class1)) == 2:
            prime.append(class1)
        if len(divisors(class2)) == 2:
            prime.append(class2)
    return prime


def alg10(end):
    """
    Check all numbers of form 3k+1 and 3k+2 up to square root of upper endpoint
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (end-2)//3+1):
        class1 = 3*i+1
        class2 = 3*i+2
        if len(divisorsfast(class1)) == 2:
            prime.append(class1)
        if len(divisorsfast(class2)) == 2:
            prime.append(class2)
    return prime


def numdivisors(end):
    dividends = np.arange(start=1, stop=end+1, dtype=int)
    divisors = np.arange(start=1, stop=end+1, dtype=int)
    for i in range(1, len(dividends)+1):
        ndivisors = 0
        for j in range(1, i//2+1):  # only check up to half
            if i % j ==0:
                ndivisors += 1
        divisors[i-1] = ndivisors+1 # add 1 for dividend itself
    new = np.column_stack([dividends, divisors])
    return new



# Main part

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
elif method == '6k-all':
    primes = alg5(int(end))
elif method == '6k-sqrt':
    primes = alg6(int(end))
elif method == '4k-all':
    primes = alg7(int(end))
elif method == '4k-sqrt':
    primes = alg8(int(end))
elif method == '3k-all':
    primes = alg9(int(end))
elif method == '3k-sqrt':
    primes = alg10(int(end))
elif method == 'divisors':
    primes = numdivisors(int(end))
else:
    if verbosity >= 0:
        print('Input invalid.')
if verbosity >= 1:
    print(primes)
elapsed = (time.process_time() - start)
if method != 'divisors':
    if verbosity >= 0:
        print('Detected {} prime numbers in {:.5f} seconds.'.format(len(primes), elapsed))
    if outfile is not None:
        with open(outfile, 'w', encoding='UTF-8') as f:
            f.write('# ********** Eratosthenes v{} **********\n'.format(version_str))
            f.write('# Tested integer range:   [2, {}]\n'.format(end))
            f.write('# Detected prime numbers: {}\n'.format(len(primes)))
            f.write('# Applied method:         {}\n'.format(method))
            f.write('# Sifting time:           {} seconds\n'.format(elapsed))
            f.write('# **************************************************\n')
            for i in range(len(primes)):
                f.write('{}\n'.format(primes[i]))
else:
    if verbosity >=0:
        print('Created divisor list in the rage [1, {}] in {:5f} seconds'.format(end, elapsed))
    if outfile is not None:
        with open(outfile, 'w', encoding='UTF-8') as f:
            f.write('# ********** Eratosthenes v{} **********\n'.format(version_str))
            f.write('# Integer range:   [2, {}]\n'.format(end))
            f.write('# Applied method:  {}\n'.format(method))
            f.write('# Time:            {} seconds\n'.format(elapsed))
            f.write('# **************************************************\n')
            f.write('# Number\tDivisors\n')
            for i in range(len(primes)):
                f.write('{}\t{}\n'.format(primes[i][0], primes[i][1]))

