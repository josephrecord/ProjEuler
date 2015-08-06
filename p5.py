##import math
##
##def gcd(a,b):
##
##    if a > b:
##        c = b
##        b = a
##        a = c
##
##    rem = 1
##
##    while rem != 0:
##        rem = b%a
##        b = a
##        a = rem
##        if rem == 0:
##            gcd = b
##
##    return gcd
##
##
##def lcm(a,b):
##
##    return a / gcd(a,b) * b
##
##
##def lcmm(*args):
##    return reduce(lcm, args)

import functools

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return functools.reduce(lcm, args)




    
