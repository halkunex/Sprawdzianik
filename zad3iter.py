a = int(input("Podaj ilość wyrazów ciągu: "))
b = 1

for i in range(0, a):
    print(i, b)
    b = (b * 2) + 1
