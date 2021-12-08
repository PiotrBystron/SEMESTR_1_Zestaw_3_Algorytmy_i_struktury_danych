T = [45, 21, 12, 41, 25, 18, 9, 31, 99, 5, 87, 24]

dlugosc = len(T)

def Min_rek(T, dlugosc):
    if dlugosc == 1:
        return T[0]
    return min(Min_rek(T, dlugosc-1), T[dlugosc-1])

print(Min_rek(T,dlugosc))