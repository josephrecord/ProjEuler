import math

num = 600851475143
upperLim = math.floor( math.sqrt(num) )
largestFac = 1

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(3, upperLim):
	if num % i == 0 and is_prime(i) == True:
		largestFac = i

print(largestFac)