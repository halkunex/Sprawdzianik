def cionk(x):
    if x == 0 or x == 1 or x == 2:
        return 1
    else:
        return cionk(x-1) + cionk(x-2) + cionk(x-3)


a = int(input("Podaj ilość wyrazów: "))

for i in range(a):
    print(i, cionk(i))
