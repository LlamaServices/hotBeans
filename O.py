# 92 poena
from itertools import permutations

lst = [int(x) for x in input().split()]
#lst = [7, 1, 6, 2, 3, 9]
maxi = 0
indi = 0

for index, x in enumerate( [ x for x in permutations(lst, 2) if lst.index(x[1]) > lst.index(x[0]) and x[0] < x[1] ] ):
    if x[1] - x[0] > maxi:
        maxi = x[1] - x[0]
        indi = index

print(maxi)