import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primeSum = 2

for i in range(3, 2000000):
    if is_prime(i) == True:
        primeSum = primeSum + i

