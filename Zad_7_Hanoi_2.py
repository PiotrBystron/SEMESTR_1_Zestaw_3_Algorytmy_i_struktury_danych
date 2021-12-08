#liczba krążków
krazki = 3

#miejsce początkowe
poczatkowe = 1 

#miejsce docelowe
docelowe = 2

#kroki = 0

def Hanoi(krazki, poczatkowe, docelowe):
    if krazki == 1:
        print("Krążek nr 1 z miejsca", poczatkowe, "na miejsce", docelowe)
    else:
        #tymczasowe = miejsce poczatkowe + miejsce docelowe + miejsce tymczasowe = 1+2+3 = 6
        tymczasowe = 6 - poczatkowe - docelowe
        Hanoi(krazki-1, poczatkowe, tymczasowe)
        print("Krążek nr", krazki, "z miejsca", poczatkowe, "na miejsce", docelowe)
        Hanoi(krazki-1, tymczasowe, poczatkowe)

print(Hanoi(krazki, poczatkowe, docelowe))