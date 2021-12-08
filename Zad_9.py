def mini_max_dzzw(T,l,r):
    if l==r:
        return T[l]
    m=(l+r)//2
    mini2 = mini_max_dzzw(T,l,m)
    mini1 = mini_max_dzzw(T,m+1,r)
    max1 = mini_max_dzzw(T,l,m)
    max2 = mini_max_dzzw(T,m+1,r)
    if mini1 < mini2:
        return mini1
    else:
        return mini2

    if max1 < max2:
        return max1
    else:
        return max2

T = [45, 21, 12, 41, 25, 18, 9, 31, 99, 87, 24]

print(mini_max_dzzw(T,0,len(T)-1))