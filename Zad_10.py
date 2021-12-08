def Scalanie(T, Lewy, Srodek, Prawy):
    n1 = Srodek - Lewy + 1
    n2 = Prawy- Srodek
  
    # tablice tymczasowe
    Lewa_tablica = [0] * (n1)
    Prawa_tablica = [0] * (n2)
  
    # kopiowanie do tymczasowych tablic
    for i in range(0 , n1):
        Lewa_tablica[i] = T[Lewy + i]
    for j in range(0 , n2):
        Prawa_tablica[j] = T[Srodek + 1 + j]
  
    # łączenie tablic tymczasowych do tablicy T
    i = 0     # pierwszy indeks pierwszej tablicy tymczasowej L
    j = 0     # pierwszej indeks drugi tablicy tymczasowej P
    k = Lewy    # pierwszy indeks połączonej tablicy
  
    while i < n1 and j < n2 :
        if Lewa_tablica[i] <= Prawa_tablica[j]:
            T[k] = Lewa_tablica[i]
            i += 1
        else:
            T[k] = Prawa_tablica[j]
            j += 1
        k += 1

    while i < n1: # kopiowanie pozotałych danych z tymczasowej L
        T[k] = Lewa_tablica[i]
        i += 1
        k += 1

    while j < n2: # kopiowanie pozotałych danych z tymczasowej P
        T[k] = Prawa_tablica[j]
        j += 1
        k += 1

def Max_rek_dzielenie(T, Lewy, Prawy):
    if Lewy < Prawy:
        Srodek = ((Lewy+Prawy)//2)
        Max_rek_dzielenie(T, Lewy, Srodek)
        Max_rek_dzielenie(T, Srodek+1, Prawy)
        Scalanie(T, Lewy, Srodek, Prawy)
    return T

T = [59, 4, 5, 45, 21, 12, 41, 25, 18, 9, 31]

print(Max_rek_dzielenie(T, 0, len(T)-1))