import math

def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True


max_primes = 0




for a in range(-1000, 1000):

	for b in range(-1000, 1000):

		prime_count = 0

		for n in range(0, 42):
		
			y = n**2 + a*n + b

			#print(a, b, n, y, is_prime(abs(y)))
			
			if is_prime(abs(y)) == True:
				prime_count += 1
				if prime_count > max_primes:
					max_primes = prime_count
					print(a, b)
			else:
				break
		

print(max_primes)