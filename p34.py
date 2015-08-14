import math

res = []

for n in range(3,999999):
	x = str(n)
	l = len(x)
	s = []
	for i in range(0, l):
		f = math.factorial(int(x[i]))
		s.append(f)
	if sum(s) == n:
		res.append(n)

print(sum(res))