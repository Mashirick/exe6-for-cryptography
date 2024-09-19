def my_pow(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return pow(a, b, c)

def Miller_Rabin(n):
    assert(type(n) == int)
    a = 3
    if n % 2 == 0:
        return True
    elif n % a == 0:
        return True
    else:
        q = n - 1
        k = 0
        while q % 2 == 0:
            q = q // 2
            k += 1
        a = my_pow(a, q, n)
        if a % n == 1:
            return False
        else:
            for i in range(k):
                if a % n == n - 1:
                    return False
                a = my_pow(a, 2, n)
            return True

def n_print(n):
    if Miller_Rabin(n):
        print(n,'is composite.')
    else:
        print(n,'is probably a prime number.')

if __name__ == '__main__':
    n1 = 202767145582614733733139403843879254621949551824058993311339593493341055229837512127224893854863968851947003448487753250093654475567042186503162873426359974273751871978241831537235413710389881550750303525056818030281312537212445925881220354174468221605146327969430834440565497127875070636801598203824198219369
    n2 = 128616849478472881130430353953064500678523243068644412259304172167157284797865859812152189162655740494781624251290671223759405322417257255428805728369829694556703036016110583498515217672808894238168137605927132353092295260773913710802957965366638715103023647160683663838567675754841243928875364791502241515843
    n_print(n1)
    print()S
    n_print(n2)

                

