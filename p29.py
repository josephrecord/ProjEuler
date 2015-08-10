a = range (2, 101)
b = range (2, 101)

x = [0]*99*99
count = 0

for i in a:
	for j in b:
		x[count] = i**j
		count = count + 1

print(len(set(x)))