T = [45, 21, 12, 41, 1, 25, 18, 9, 31, 99, 5, 87, 24, 0]

dlugosc = len(T)

def Min_rek(T, dlugosc):
    if dlugosc == 1:
        return T[0]
    return min(T[dlugosc-1], Min_rek(T, dlugosc-1) )

print(Min_rek(T,dlugosc))


#poprawne
def min_rek2(T):
    if len(T) == 1:
        return T[0]
    else:
        return min(T[0], min_rek2(T[1:]))

print(min_rek2(T)) 