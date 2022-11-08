# 40 poena
from statistics import median
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
flist = list1 + list2
del list1
del list2
flist.sort()
print(median(flist))