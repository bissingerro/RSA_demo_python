
import random
import math
import time


# range for prime number generation
MIN = 2**15
MAX = 2**16


class Keypair:
    def __init__(self, public, private, modulus) -> None:
        self.public = public
        self.private = private
        self.modulus = modulus
    def __repr__(self) -> str:
        s = f"PubKey: {self.public}, SecKey: {self.private}, Modulus: {self.modulus}"
        return s
    def __str__(self) -> str:
        return self.__repr__()


def isPrime(x):
    """returns True if x is prime"""
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def ggT(a,b):
    """Returns the greatest common divisor of a and b"""
    while b:
        a,b = b, a % b
    return a
        

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
            print("And again")
            genPrimeOfSize(min, rand)

    return prime

def mul_inverse(n,x):
    a = [n,x]
    d = [0,0]
    y = [0,1]
    i = 2
    while a[-1] != 0:
        a.append(a[i-2] % a[i-1])
        d.append(a[i-2] // a[i-1])
        i += 1
    for i in range(2, len(d) -1):
        y.append(y[i-2] - (d[i]*y[i-1]))
    return y[-1]




def genKeyPair():
    print("started keygen")
    t = time.time()
    p = genPrimeOfSize(MIN,MAX)
    q = genPrimeOfSize(MIN,MAX)
    while abs(p - q) < (abs(MIN-MAX)/10):
        q = genPrimeOfSize(MIN,MAX)
    print("generated p:",p, time.time()-t)
    print("generated q:", p, time.time()-t)
    n = p * q
    print("n: ", n)
    phi_of_n = (p -1 ) * (q - 1)
    print("phi of n: ", phi_of_n)
    e = random.randint(max((p,q)), phi_of_n)
    while ggT(phi_of_n, e) != 1:
        e += 1
        if e >= phi_of_n:
            e = random.randint(1, phi_of_n)
    print("calculated e:", e, time.time()-t)
                
    #k = random.randint(1000,n)
    #while k == e:
     #   k = random.randint(1,n)
    
    d = mul_inverse(e, phi_of_n) % phi_of_n
    
    print("generated private key, keygen done", time.time()-t)
    return Keypair(e, d, n)

def enc(message, pubKey, modulus):
    return (message**pubKey) % modulus

def dec(ciphretext, secKey, modulus):
    return (ciphretext**secKey) % modulus