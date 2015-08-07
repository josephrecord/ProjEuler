import math

def tri(n):
    t = 0
    while n > 0:
        t = t + n
        n = n - 1
    return t

def numfactors(n):
    upperlim = int(math.sqrt(n)) + 1
    result = set()
    for i in range(1, upperlim):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return len(result)


n = 1
while True:
    num = numfactors(tri(n))
    if num >= 500:
        print(tri(n))
        break
    n = n + 1
        
    
