import math

def gcd(a,b):

    if a > b:
        c = b
        b = a
        a = c

    rem = 1

    while rem != 0:
        rem = b%a
        b = a
        a = rem
        if rem == 0:
            gcd = b

    return gcd


def lcm(a,b):

    return a / gcd(a,b) * b


def lcmm(*args):
    return reduce(lcm, args)







    
