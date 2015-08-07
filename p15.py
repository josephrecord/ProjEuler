# n by n grid
def countroutes(n):
    result = 1
    for i in range(1,n+1):
        result = result * (n+i)/i
    return result

print(countroutes(20))