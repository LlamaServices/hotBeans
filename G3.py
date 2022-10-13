l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l = l1+l2

for x in l:
    if l.count(x) > 1: pass
    else:
        print(x)
        break