# x = [[a,b,c,d,e,f,g,h] for a in range(0,201) for b in range(0,101) for c in range(0,41) for d in range(0,21) for e in range(0,11)\
# for f in range(0,5) for g in range(0,3) for h in range(0,2)\
# if a + 2*b + 5*c + 10*d + 20 *e + 50*f + 100*g + 200*h == 200 and\
# a+b+c+d+e+f+g+h<201]

# print(x, len(x))

from time import time

t = time()

p = 200

x = [[a,b,c,d,e,f,g] for a in range(0,p+1) for b in range(0,(p//2)+1) for c in range(0,(p//5)+1) for d in range(0,(p//10)+1) for e in range(0,(p//20)+1) for f in range(0,(p//50)+1) for g in range(0,(p//100)+1)\
if a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g  == p and\
a+b+c+d+e+f+g<p+1]

print(len(x), time()-t)