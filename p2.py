tot = 2
c = 0
a = 1
b = 2

while True:

        c = a + b

        if c > 4000000:
                break

        
        if c%2 == 0:
                tot = tot + c

        print(c,tot)

        a = b
        b = c
