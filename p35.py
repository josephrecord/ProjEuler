import math
from collections import deque

def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def mk_list(n):
	# convert int into a list of strings of the digits
	# e.g. n = 197, result = ['1', '9', '7']
	s = str(n)
	ls = []
	for digit in s:
		ls.append(digit)
	return ls

def mk_num(list):
	s = map(str, list)
	s = ''.join(s)
	s = int(s)
	return s


def rotate(num, t):
	rotator = mk_list(num)
	rotator = deque(rotator)
	for i in range(0,t):
		rotator.rotate(-1)
	return mk_num(list(rotator))

print(rotate(197112365, 1122132))


# for n in range(2, 100):
# 	print(n, is_prime(n))