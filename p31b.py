coins = [1, 2, 5, 10, 20, 50, 100, 200]
amt = 200

def ways(target, i):
	if i <= 0:
		return 1
	res = 0
	while target >= 0:
		res = res + ways(target, i-1)
		target = target - coins[i]
	return res

print(ways(amt, 7))