import math
import time
from itertools import combinations_with_replacement

def factors(n):
    upperlim = int(math.sqrt(n)) + 1
    result = set()
    for i in range(1, upperlim):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

def is_abund(n):
	f = factors(n)
	s = sum(f) - n
	if s > n:
		return True
	else:
		return False


t = time.time()

a = [0]*28124
b = [0]*6965
s = 0
acount = 0
ncount = 0
sums = 0

for i in range(0, 28124):
	if is_abund(i) == True:
		a[i] = (i, True)
		acount = acount + 1
		b[acount-1] = i
	else:
		a[i] = (i, False)
		s = s + 1


c = list(combinations_with_replacement(b, 2))

for i in range(0, len(c)):
	c[i] = sum(c[i])

c = set(c)

c = [x for x in c if x <= 28123]

tot = sum(range(1, 28124))
csum = sum(c)

sum_of_not_sum_of_two_ab = tot-csum

print(sum_of_not_sum_of_two_ab, time.time()-t)