def matching_digit(a,b):
	if a%10 != 0 and b%10 !=0:
		a, b = str(a), str(b)
		if a[0] == b[0] or a[0] == b[1] or a[1] == b[0] or a[1] == b[1]:
			return True
		else:
			return False
	return False

def find_mathcing(a,b):
	res = list()
	a, b = str(a), str(b)
	if a[0] == b[0]:
		res.append((0, 0))
	if a[0] == b[1]:
		res.append((0, 1))
	if a[1] == b[0]:
		res.append((1, 0))
	if a[1] == b[1]:
		res.append((1, 1))
	return res

def cancel_digit(a,b):
	if matching_digit(a,b) == True:
		a, b = str(a), str(b)
		match = find_mathcing(a,b)
		num_matches = len(match)

		if match[0][0] == 0:
			a = a[1]
		if match[0][0] == 1:
			a = a[0]
		if match[0][1] == 0:
			b = b[1]
		if match[0][1] == 1:
			b = b[0]

		if int(a) != 0 and int(b) != 0:
			return int(a)/int(b)

x = list()

for m in range(11,100):
	n = 10
	while n > 9 and n < m:
		if matching_digit(n,m) == True:
			#print(n,m, n/m, cancel_digit(n,m))
			if n/m == cancel_digit(n,m):
				#print(n,m,"match!")
				x.append([n,m])
		n += 1

print(x)
print(x[0][0]*x[1][0]*x[2][0]*x[3][0], x[0][1]*x[1][1]*x[2][1]*x[3][1])