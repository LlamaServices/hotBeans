# 100 poena (daje 96 tokom provere koda, a posle pise 100 na pregledu, tako da nznm)
l = [int(x) for x in input().split()]
m = []
count = 1
for x in range(1, len(l)):
    if l[x] < l[x-1]:
        count+=1
    else:
        m.append(count)
        count = 1
print(max(m))
