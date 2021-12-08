#liczba krążków
krazki = 3

a = ["A"]
b = ["B"]
c = ["C"]

def Hanoi(krazki, a, b, c):
    if krazki == 1:
        print(a, b)
    else:
        Hanoi(krazki-1, a, c, b)
        print(a, b)
        Hanoi(krazki-1, c, b, a)

print(Hanoi(krazki, a, b, c))