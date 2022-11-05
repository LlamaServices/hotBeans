# 38 poena
niz = [int(x) for x in input().split()]
duzina = 1
maxi = 0
for index in range(1, len(niz)):
    if niz[index] > niz[index-1]:
        duzina += 1
    else:
        if duzina > maxi:
            maxi = duzina
        duzina = 1
if duzina > maxi: maxi = duzina
print(maxi)