def funk(cilj, niz):
    for x in niz:
        for y in niz:
            if x+y==cilj:
                return (x, y)
    return -1

cilj = 5
niz  = [1, 2, 3, 4, 5]
print(funk(cilj, niz))