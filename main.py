import rsa

if __name__ == "__main__":

    k = rsa.genKeyPair()
    print(k)
    t = 15
    c = (t**k.public) % k.modulus
    t2 = (c**k.private) % k.modulus
    print(t)
    print(c)
    print(t2)
    