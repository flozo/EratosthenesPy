import numpy as np

class Algorithm(object):
    """
    Define algorithm class with divisor method and sieve method.
    Divisor method can be: sqrt(default), all.
    Sieve method can be: all, 6k(default), 4k, 3k, odd.
    """
    def __init__(self, divisormethod='sqrt', sievemethod='6k'):
        self.divisormethod = divisormethod
        self.sievemethod = sievemethod


# Divisor algorithms

def divisors_all(number):
    """
    Determine divisors of number up to number
    """
    divs = []
    if number < 1:          # 0 has no divisors
        return divs
    elif number >= 1:       # 1 is always divisor for number >= 1
        divs.append(1)
    if number >= 2:
        for i in range(2, number):
            if number % i == 0:
                divs.append(i)
        divs.append(number) # number itself is always divisor
    return divs


def divisors_sqrt(number):
    """
    Determine all divisors of number up to square root of number
    """
    divs = []
    if number < 1:          # 0 has no divisors
        return divs
    elif number >= 1:       # 1 is always divisor for number >= 1
        divs.append(1)
    if number >= 2:
        for i in range(2, int(np.sqrt(number))+1):
            if number % i == 0:
                divs.append(i)
        divs.append(number) # number itself is always divisor
    return divs


def isprime(number):
    """
    Just check if number is prime
    """
    if len(divisors_sqrt(number)) == 2:
        return True
    else:
        return False


# Sieve algorithms

def alg_all(divisorfunc, limit):
    """
    Check all numbers
    """
    prime = []
    for i in range(2, limit+1):
        if len(divisorfunc(i)) == 2:
            prime.append(i)
    return prime


def alg_odd(divisorfunc, limit):
    """
    Check only odd numbers
    """
    prime = []
    prime.append(2)
    for i in range(3, limit+1, 2):
        if len(divisorfunc(i)) == 2:
            prime.append(i)
    return prime


def alg_6k(divisorfunc, limit):
    """
    Check all numbers of form 6k-1 and 6k+1
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (limit-1)//6+1):
        class1 = 6*i-1
        class2 = 6*i+1
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        if len(divisorfunc(class2)) == 2:
            prime.append(class2)
    return prime


def alg_4k(divisorfunc, limit):
    """
    Check all numbers of form 4k+1 and 4k+3
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (limit-3)//4+1):
        class1 = 4*i+1
        class2 = 4*i+3
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        if len(divisorfunc(class2)) == 2:
            prime.append(class2)
    return prime


def alg_3k(divisorfunc, limit):
    """
    Check all numbers of form 3k+1 and 3k+2
    """
    prime = []
    prime.append(2)
    prime.append(3)
    for i in range(1, (limit-2)//3+1):
        class1 = 3*i+1
        class2 = 3*i+2
        if len(divisorfunc(class1)) == 2:
            prime.append(class1)
        if len(divisorfunc(class2)) == 2:
            prime.append(class2)
    return prime


def numdivisors(end):
    """
    Determine the number of divisors of a number
    """
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

