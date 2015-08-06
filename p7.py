import math

numPrimes = 6
startNum = 14

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

while numPrimes < 10001:
    if is_prime(startNum):
        numPrimes = numPrimes + 1
    startNum = startNum + 1

    


