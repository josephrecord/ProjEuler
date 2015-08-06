biggest = 1
for i in range(999,1,-1):
    for j in range(999,1,-1):
        n = i*j
        if str(n) == str(n)[::-1] and n > biggest:
            biggest = n
            print(biggest)
