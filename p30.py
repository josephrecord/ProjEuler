from time import time

def list_to_int(x):
	l = len(x)
	result = 0
	dgt = 1
	for i in range(l-1, -1, -1):
		result = result + x[i]*dgt
		dgt = dgt * 10
	return result

t = time()

n = range(0,10)

s = 0

x = [[z,a,b,c,d,e] for z in n for a in n for b in n for c in n for d in n for e in n\
if z**5 + a**5 + b**5 + c**5 + d**5 + e**5 == ((100000*z)+ (10000*a) + (1000*b) + (100*c) + (10*d) + e)]

for i in range(0, len(x)):
	s = list_to_int(x[i]) + s

print(s-1)