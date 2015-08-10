def seq_len(d):
	x = 9
	z = x
	k = 1
	while z % d:
		z = z * 10 + x
		k = k + 1
	return k, z / d



denom = range(990, 400, -1)

# x = [0]*len(denom)

# count = 0

# for i in denom:
# 	x[count] = [1/i]
# 	count = count + 1


y = [x for x in denom if x % 2 != 0 and x % 5 != 0 and x > 367]
len_y = len(y)

print(y)

max_seq = 0

for i in range(0, len_y-1):
	print(y[i], seq_len(y[i]))