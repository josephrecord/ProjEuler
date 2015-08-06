sumofsquares = 0 

for i in range(1,101):
    x = i*i
    sumofsquares = sumofsquares + x

y = sum(range(1,101))
sqaureofsums = y*y

ans = sqaureofsums - sumofsquares

print(ans)
