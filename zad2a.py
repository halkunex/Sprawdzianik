def cionk(x):
    if x == 0:
        return 4
    else:
        return 3 + cionk(x-1)


a = int(input("Podaj ilość wyrazów: "))

for i in range(a):
    print(i, cionk(i))
