#!/usr/bin/python3
l1 = [float(x) for x in input().split()]
l2 = [float(x) for x in input().split()]

if len(l1) > len(l2):
    b = l1
    s = l2
else:
    b = l2
    s = l1

for x in b:
    if x in s:
        pass
    else:
        secret = x
        break

print(int(secret))
