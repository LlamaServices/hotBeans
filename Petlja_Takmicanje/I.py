# 38 poena
def meow(niz):
    lenght = 1
    maxi = 1
    for x in range(1, len(niz)):
        if niz[x-1] > niz[x]:
            lenght+=1
        else:
            if lenght > maxi:
                maxi = lenght
            lenght = 1
        if niz[x] == niz[-1]:
            if lenght > maxi:
                maxi = lenght
            lenght = 1
    return maxi

niz = [int(x) for x in input().split()]
print(meow(niz))