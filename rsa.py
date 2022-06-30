import imp
import random
import math


def isPrime(x):
    """returns True if x is prime"""
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def genPrimeOfSize(min, max):
    """returns a large pseudorandom prime number as int or -1"""
    if min == max:
        print("no prime found in given range/ range to small")
        return -1
    rand = random.randint(min, max) # random number in given range
    prime = rand

    if prime % 2 == 0:
        prime += 1
    # searching the prime number
    while not isPrime(prime):
        prime += 2
        if prime > max:
            genPrimeOfSize(min, rand)

    return prime


def genKeyPair():
    p = genPrimeOfSize( 2**10,2**11)
    q = genPrimeOfSize(2**10, 2**11)
    n = p * q
    
    return p,q