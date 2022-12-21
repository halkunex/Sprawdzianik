def cionk(x):
    if x == 0:
        return 2
    else:
        return 2 * cionk(x-1)


a = int(input("Podaj ilość wyrazów: "))

for i in range(a):
    print(i, cionk(i))
