import random

def isPrime(x):
    """returns True if x is prime"""
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

    pass

def genPrimeOfSize(min, max):
    """returns a large pseudorandom prime number as int or -1"""
    if min == max:
        print("no prime found in given range")
        return -1
    rand = random.randint(min, max) # random number in given range
    x = random.choice((-1, +1)) # going up or donwarts
    prime = rand
    
    searching the prime number
    while not isPrime(prime):
        prime += x
        if prime > max:
            genPrimeOfSize(min, rand);
        elif prime < min:
            genPrimeOfSize(rand, max)

    return prime


