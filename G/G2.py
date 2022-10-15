l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
b = s = list()
if len(l1)>len(l2): b, s = l1, l2
else: s, b = l1, l2
meow = set(b).difference(s)
for x in meow:
    break
print(x)
