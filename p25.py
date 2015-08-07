def fib(n):

    a, b = 0, 1
    
    for i in range(n):
        a, b = b, a+b
    return a


n = 1

while True:
    if len(str(fib(n))) == 1000:
        print(n)
        break
    n = n + 1