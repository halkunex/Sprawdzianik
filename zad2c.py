def cionk(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return cionk(x-1) - cionk(x-2)


a = int(input("Podaj ilość wyrazów: "))

for i in range(a):
    print(i, cionk(i))
