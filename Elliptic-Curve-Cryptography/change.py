def stringToInt(s):
    n = 0
    for i in range(0,len(s)):
        n *= 100
        n += ord(s[i]) - 32
    return n

def intToString(n):
    s = ""
    while(n > 0):
        num = n % 100
        a = str(chr(num + 32))
        a += s
        s = a
        n /= 100
    return s
