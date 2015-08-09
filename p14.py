def coll(n):
    count = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n)+1
        count = count + 1
    return count

chainlen = 0
n = 0
for i in range(1, 1000000):
    if coll(i) > chainlen:
        chainlen = coll(i)
        n = i

print(chainlen, n)