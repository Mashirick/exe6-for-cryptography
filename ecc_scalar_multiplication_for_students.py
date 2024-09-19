from Crypto.Util.number import inverse


def pt_add(p, q, E):
    zero = (0, 0)
    x3, y3 = 0, 0

    # TODO
    a = E['a']
    mod = E['p']
    x1, y1 = p
    x2, y2 = q
    if p == zero:
        return q
    elif q == zero:
        return p
    else:
        if p == q:
            k = (3 * x1 ** 2 + a) * inverse(2 * y1, mod) % mod
        else:
            k = (y2 - y1) * inverse(x2 - x1, mod) % mod
        
    x3 = (k ** 2 - x1 - x2) % mod
    y3 = (k * (x1 - x3) - y1) % mod    
        
    return x3, y3

def scalar_mult(n, p, E):
    q, r = p, (0, 0)
    # TODO
    while 1:
        if n % 2 == 1:
            r = pt_add(r, q, E)
        q = pt_add(q, q, E)
        n = n // 2
        if n == 0:
            break
    return r
    

if __name__ == '__main__':
    E = {'a': 497, 'b': 1768, 'p': 9739}

    x = (5323, 5438)

    assert scalar_mult(1337, x, E) == (1089, 6931)

