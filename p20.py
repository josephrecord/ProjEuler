import math
from time import time

def sum_digits(n):
	# Sum the digits of int n
	s = 0
	while n:
		n, rem = divmod(n, 10)
		s += rem
	return s

t = time()

n = 100
f = math.factorial(n)
f = sum_digits(f)

print(f, time()-t)