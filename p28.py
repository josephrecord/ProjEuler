

ur = [x**2 for x in range(3, 1003, 2)]

l = len(ur)
print(l)

ul = [0]*l
dl = [0]*l
dr = [0]*l

sub1 = 2
sub2 = 4
sub3 = 6

for i in range(0, l):
	
	ul[i] = ur[i] - sub1
	dl[i] = ur[i] - sub2
	dr[i] = ur[i] - sub3
	sub1 = sub1 + 2
	sub2 = sub2 + 4
	sub3 = sub3 + 6

print(sum(dr)+sum(dl)+sum(ul)+sum(ur)+1)