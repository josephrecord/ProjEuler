ans = [(a,b,c) for c in range(1,500) for b in range(1,c) for a in range(1,b)\
 if a*a + b*b == c*c and a + b + c == 1000]

p = 1
for i in range(0,3):
    p = p * ans[0][i]

print(p)