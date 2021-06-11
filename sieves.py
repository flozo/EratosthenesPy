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
    divs.append(1)      # 1 is always divisor
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
    divs.append(1)      # 1 is always divisor
    for i in range(2, int(np.sqrt(number))+1):
        if number % i == 0:
            divs.append(i)
    divs.append(number) # number itself is always divisor
    return divs


# Sieve algorithms
def alg1(end):
    """
    Check all numbers up to upper endpoint
    """
    prime = []
    for i in range(2, end+1):
        if len(divisors_all(i)) == 2:
            prime.append(i)
    return prime


def alg2(end):
    """
    Check all numbers up to square root of upper endpoint
    """
    prime = []
    for i in range(2, end+1):
        if len(divisors_sqrt(i)) == 2:
            prime.append(i)
    return prime


def alg3(end):
    """
    Check only odd numbers up to upper endpoint
    """
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisors_all(i)) == 2:
            prime.append(i)
    return prime


def alg4(end):
    """
    Check only odd numbers up to square root of upper endpoint
    """
    prime = []
    prime.append(2)
    for i in range(3, end+1, 2):
        if len(divisors_sqrt(i)) == 2:
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
        if len(divisors_all(class1)) == 2:
            prime.append(class1)
        if len(divisors_all(class2)) == 2:
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
        if len(divisors_sqrt(class1)) == 2:
            prime.append(class1)
        if len(divisors_sqrt(class2)) == 2:
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
        if len(divisors_all(class1)) == 2:
            prime.append(class1)
        if len(divisors_all(class2)) == 2:
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
        if len(divisors_sqrt(class1)) == 2:
            prime.append(class1)
        if len(divisors_sqrt(class2)) == 2:
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
        if len(divisors_all(class1)) == 2:
            prime.append(class1)
        if len(divisors_all(class2)) == 2:
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
        if len(divisors_sqrt(class1)) == 2:
            prime.append(class1)
        if len(divisors_sqrt(class2)) == 2:
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

