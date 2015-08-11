t = []
for line in open("p067_triangle.txt"):
	t.append(list(map(int, line.split())))



print(t)


for i in range(len(t)-1, 0, -1):
	for j in range(0, len(t[i-1])):
		t[i-1][j] = t[i-1][j] + max(t[i][j], t[i][j+1])

print(t[0][0])