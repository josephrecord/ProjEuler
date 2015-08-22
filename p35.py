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
	# inverse operation of mk_list
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

def is_circ_prime(n):
	str_n = str(n)
	size_n = len(str_n)
	num_rotates = size_n
	count = 0

	for i in range(0, num_rotates):
		test_prime = rotate(n, i)
		if is_prime(test_prime) == False:
			return False
		elif is_prime(test_prime) == True and count == num_rotates-1:
			return True
		count += 1


county = 0
for n in range(2, 1000001):
	if is_circ_prime(n) == True:
		print(n)
		county += 1
print(county)