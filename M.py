from statistics import median
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
flist = list1 + list2
flist.sort()
print(median(flist))

'''
from statistics import median
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
f = list1 + list2
f.sort()
if len(f) % 2 == 0: x = (f[len(f)/2] + f[len(f)/2+1]) / 2
else: x = f[int(len(f)/2)]
print(x)
'''