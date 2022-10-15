from itertools import permutations

lst = [int(x) for x in input().split()]
sorted_lst = []
for index, x in enumerate(permutations(lst, 2)):
    if x[0] < x[1]: sorted_lst.append(x)

maxi = 0
indi = 0
for index, x in enumerate([x for x in sorted_lst if lst.index(x[1]) > lst.index(x[0])]):
    if x[1] - x[0] > maxi:
        maxi = x[1] - x[0]
        indi = index

print(maxi)