import math

def factors(n):
	upperlim = int(math.sqrt(n)) + 1
	result = set()
	for i in range(2, upperlim):
		quot, rem = divmod(n, i)
		if rem == 0:
			result |= {1, i, quot}
	return sorted(list(result))

def d(n):
	result = sum(factors(n))
	return result
	
s = 0
	
for i in range(1, 10000):
	x = d(i)
	y = d(x)
	if x > 0 and x < 10000 and i != x:
		if y == i:
			print('amicable', i, d(i))
			s = s + i

print(s)