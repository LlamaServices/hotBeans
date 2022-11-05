# 56 poena
l1 = set([int(x) for x in input().split()])
l2 = set([int(x) for x in input().split()])
if len(l1)>len(l2): x = l1.difference(l2)
else: x = l2.difference(l1)
print(list(x)[0])