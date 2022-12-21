def cionk(x):
    if x == 0:
        return 1
    else:
        return cionk(x-1) * 2 + 1


a = int(input("Podaj ilość wyrazów: "))

for i in range(a):
    print(i, cionk(i))
