ans = 0

for i in range(1, 1000000):
	dec = i
	binary = bin(i)[2:]
	if str(dec) == str(dec)[::-1] and str(binary) == str(binary)[::-1]:
		ans += i

print(ans)