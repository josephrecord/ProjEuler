def is_pan_dig(a,b,c):
	a, b, c = str(a), str(b), str(c)
	x = a + b + c

	if set(x) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} and len(x) == 9:
		return True
	else:
		return False


print(is_pan_dig(123,456,789))


s = 0
count = 0
prods = list()

for a in range(1,500):
	for b in range(1,2000):
		c = a * b
		if is_pan_dig(a, b, c) == True:
			prods.append(c)
			print(a,b,c)
			count += 1

print(sum(set(prods)))