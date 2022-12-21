a = int(input("Podaj ilość wyrazów ciągu: "))
b = 1
c = 1
d = 1

for i in range(0, a):
    print(i, b)
    e = b + c + d
    b = c
    c = d
    d = e
