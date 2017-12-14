def inv(a, b):
    r = [a,b]
    a = [1,0]
    while(r[1]!=0):
        q = r[0]/r[1]
        t = a[1]
        a[1] = a[0] - a[1] * q
        a[0] = t
        t = r[1]
        r[1] = r[0] % r[1]
        r[0] = t
    return a[0]

def modFraction(num, den, mod):
    # mdc(den, mod) = 1, because mod is prime
    
    return (num*inv(den, mod)) % mod
