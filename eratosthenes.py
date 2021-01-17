#!/usr/bin/env python3
#
# Eratosthenes v0.2 2021-01-17

import argparse
import time
import numpy as np

# Define argument parsers and subparsers
parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. Written by Johannes Engelmayer')
#subparsers = parser.add_subparsers(title='commands', dest='command', help='commands')

parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.2 (2021-01-17)')
#settings_parser = subparsers.add_parser('settings', aliases=['set', 'st', 's'], help='change settings')
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='verbosity level (-v, -vv, -vvv): '
                    'default = single-line output, v = multi-line, vv = detailed, vvv = array output')
parser.add_argument('-q', '--quiet', action='store_true',
                    help=('disable terminal output (terminates all verbosity)'))
parser.add_argument('-m', '--method', dest='method', choices=('all', 'sqrt', 'odd-all', 'odd-sqrt'), default='sqrt', help='sieve method')
parser.add_argument('limit', type=int, default=100, help='upper limit of test range')

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
    for i in range(2, end):
        if len(divisors(i)) == 2:
            prime.append(i)
    return prime


# check only to sqrt(n)
def alg2(end):
    prime = []
    for i in range(2, end):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime

# check only even numbers to sqrt(n)
def alg3(end):
    prime = []
    for i in range(3, end, 2):
        if len(divisorsfast(i)) == 2:
            prime.append(i)
    return prime

#end = input('Bestimme alle Primzahlen von 2 bis ')
#method = input('Benutze Algorithmus Nr. (1-3) ')
end = args.limit
method = args.method
start = time.process_time()
if method == 'all':
    primes = alg1(int(end))
elif method == 'sqrt':
    primes = alg2(int(end))
elif method == 'odd':
    primes = alg3(int(end))
else:
    if verbosity >= 0:
        print('Nicht vorhanden!')
if verbosity >= 0:
    print(primes)
elapsed = (time.process_time() - start)
if verbosity >= 0:
    print('Es wurden {} Primzahlen in {:.5f} Sekunden gefunden.'.format(len(primes), elapsed))

