import math
from itertools import combinations, permutations, combinations_with_replacement

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

# setd = sorted(set(d))

# print(setd)

c = set(c)
c = sorted(c)

c = [x for x in c if x <= 28123]

tot = sum(range(0, 28124))
csum = sum(c)

sum_of_not_sum_of_two_ab = tot-csum

print(tot, csum, sum_of_not_sum_of_two_ab)
