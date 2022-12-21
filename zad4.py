import random

random.seed(X)

for i in range(100):
    a = random.randrange(0, 6)
    b = random.randrange(0, 6)
    c = random.randrange(0, 6)
    print(a, b, c)
    if a >= b and a >= c:
        x = a
        if b >= c:
            y = b
            z = c
        else:
            y = c
            z = b
    elif b >= a and b >= c:
        x = b
        if a >= c:
            y = a
            z = c
        else:
            y = c
            z = a
    else:
        x = c
        if a >= b:
            y = a
            z = b
        else:
            y = b
            z = a
    if z == 0 or x >= y + z:
        print("Nie da się zbudować trójkąta")
    else:
        x = x*x
        y = y*y
        z = z*z
        if x == y+z:
            print("Trójkąt jest prostokątny")
        elif x > y+z:
            print("Trójkąt jest rozwartokątny")
        else:
            print("Trójkąt jest ostrokątny")
