import random

lscore, jscore = 0, 0

for i in range (1,1000000000):
    S = 0

    while True:
        a = random.random()
        S = S + a
        if S > 1:
            x = a
            break

    while True:
        b = random.random()
        S = S + b
        if S > 2:
            y = b
            break

    if x > y:
        lscore += 1

    elif y > x:
        jscore +=1

print( jscore / (lscore + jscore) )

#0.5276653805276654
        
    
