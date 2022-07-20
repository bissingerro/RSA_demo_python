from time import time
import rsa

if __name__ == "__main__":
    k = rsa.genKeyPair()
    print(k)
    t = 15
    z = time()
    c = (t**k.public) % k.modulus
    print("time encrypt:", time()-z)
    z = time()
    t2 = (c**k.private) % k.modulus
    print("time:", time()-z)
    print(t)
    print(c)
    print(t2)
    