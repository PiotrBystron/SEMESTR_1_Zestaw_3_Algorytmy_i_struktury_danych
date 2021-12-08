def minimum_dzzw(T,l,r):
    if l==r:
        return T[l]
    m=(l+r)//2
    mini2 = minimum_dzzw(T,l,m)
    mini1 = minimum_dzzw(T,m+1,r)
    if mini1 < mini2:
        return mini1
    else:
        return mini2

T = [45, 21, 12, 41, 25, 18, 9, 31, 99, 5, 87, 24]

print(minimum_dzzw(T,0,len(T)-1))