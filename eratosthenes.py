#!/usr/bin/env python3
#
# Eratosthenes v0.2 2021-01-17

import time
import numpy as np


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

end = input('Bestimme alle Primzahlen von 2 bis ')
method = input('Benutze Algorithmus Nr. (1-3) ')
start = time.process_time()
if method == '1':
    primes = alg1(int(end))
elif method == '2':
    primes = alg2(int(end))
elif method == '3':
    primes = alg3(int(end))
else:
    print('Nicht vorhanden!')
print(primes)
elapsed = (time.process_time() - start)
print('Es wurden {} Primzahlen in {:.5f} Sekunden gefunden.'.format(len(primes), elapsed))

