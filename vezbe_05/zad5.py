def funk(niz):
    maxi = abs(niz[1] - niz[0])
    for x in range(1, len(niz)):
        if abs(niz[x] - niz[x-1]) > maxi:
            maxi = abs(niz[x] - niz[x-1])
    return maxi

print(funk([1,2,3,1,5]))