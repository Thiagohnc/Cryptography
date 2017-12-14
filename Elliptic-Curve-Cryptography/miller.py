from random import randint
import math

def Miller(n1, n2):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
    primes2 = [3,5,7,11,13,17]
    comp = 1
    while(comp != 0):
        ready = 0
        while(ready == 0):
            n = randint(n1,n2)
            if(n % 2 == 0):
                n += 1
            n -= 2
            ready = 1
            for i in primes2:
                if(n%i == 0):
                    ready = 0
        prime = 1
        for b in primes:
            comp = 1
            k = 0
            q = n - 1
            while(q % 2 == 0):
                k += 1
                q /= 2
            t = pow(b,q,n)
            if(t == 1 or t == n - 1):
                comp = 0
            i = 1
            while(i < k):
                t = pow(t,2,n)
                if(t == n-1):
                    comp = 0
                i += 1
            if(comp == 1):
                break
    return n
