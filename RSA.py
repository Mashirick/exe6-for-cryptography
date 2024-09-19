from math import gcd
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def my_pow(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return pow(a, b, c)

def get_e(n):
    e = 2
    while e < n:
        if gcd(e, n) == 1:
            return e
        e += 1
    return e
def get_d(x, n):
    '''
    d = 1
    while d < n:
        if (x * d) % n == 1:
            return d
        d += 1
    '''
    return inverse(x, n)

def RSA_Key(p, q):
    assert(type(p) == int)
    assert(type(q) == int)
    assert( p != q)

    n = p * q
    fai = (p - 1) * (q - 1)
    e = get_e(fai)
    d = get_d(e, fai)

    PbK = (e, n)
    PrK = d
    print('n: ', n)
    print('e: ', e)
    return PbK, PrK

def RSA_Encryption(P, PbK):
    e, n = PbK
    assert(type(P) == int)
    assert(type(e) == int)
    assert(type(n) == int)
    assert(P < n)

    return my_pow(P, e, n)

def RSA_Decryption(C, PrK, n):
    d = PrK
    assert(type(C) == int)
    assert(type(d) == int)
    assert(type(n) == int)
    
    return my_pow(C, d, n)
    
def RSA(P, length):
    p = getPrime(length)
    q = getPrime(length)
    n = p * q
        
    PbK, PrK = RSA_Key(p, q)
    C = RSA_Encryption(P, PbK)
    P = RSA_Decryption(C, PrK, n)
    return C, P
    

if __name__ == '__main__':
    secrets = b"Applied_Cryptography"
    length = 256
    
    P = secrets
    P = bytes_to_long(secrets)
    C, P = RSA(P, length)
    P = long_to_bytes(P)
    
    print(f'密文：{C}')
    print(f'明文：{P}')