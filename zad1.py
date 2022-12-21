def NWD(x, y):
    while x != 0:
        pom = x
        x = y % x
        y = pom

    return y


a = int(input("Podaj licznik pierwszej liczby: "))
b = int(input("Podaj mianownik pierwszej liczby: "))
c = int(input("Podaj licznik drugiej liczby: "))
d = int(input("Podaj mianownik drugiej liczby: "))
e = 0
f = 0

if b == 0 or d == 0:
    print("Ułamek nie może mieć w mianowniku 0")
else:
    a = a * int(d/NWD(b, d))
    b = int(d/NWD(b, d)*b)
    c = c * int(b/NWD(b, d))
    d = int(b/NWD(b, d)*d)

    e = (a+c) / NWD(a+c, b)
    f = b / NWD(a+c, b)

    print(str(int(e)) + "/" + str(int(f)))
