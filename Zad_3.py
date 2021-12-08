def suma_skladnikow (x):
    if x == 1:
        return 1
    elif x%2 == 0:
        return 1/x + suma_skladnikow(x-1)
    else:
        return -1*(1/x) + suma_skladnikow(x-1)

x = int(input("Podaj liczbę n składników: "))

print(suma_skladnikow(x))
