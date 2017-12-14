from mod import modFraction

def addPoints(pointA, pointB, A, B, p):

    if(pointA == "neutral"):
        return pointB
    if(pointB == "neutral"):
        return pointA
    if((pointA[0] == pointB[0]) & (pointA[1] == -pointB[1])):
        return "neutral"

    if(pointA != pointB):
        slope = modFraction(pointB[1] - pointA[1], pointB[0] - pointA[0], p)
    else:
        slope = modFraction(3*pointA[0]*pointA[0] + A, 2*pointA[1], p)

    x3 = (slope*slope - pointA[0] - pointB[0]) % p
    y3 = (slope*(pointA[0] - x3) - pointA[1]) % p
    pointC = (x3, y3)
    return pointC

def doubleAndAdd(pointA, n, A, B, p):
    # A e B are constants of Elliptic Curve y^2 = x^3 + Ax + B
    # Returns n*pointA on Elliptic Curve over field Fp

    pointQ = "neutral"
    while(n > 0):

        if(n % 2 == 1):
            pointQ = addPoints(pointQ, pointA, A, B, p)

        pointA = addPoints(pointA, pointA, A, B, p)
        n /= 2

    return pointQ
