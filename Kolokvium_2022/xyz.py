def find(arr):
    arr.sort()
    x = arr[0]
    y = arr[1]
    xyz = arr[-1]
    z = xyz - (x+y) 
    return "{0} {1} {2}".format(x, y, z)

#print(find([int(x) for x in input().split()]))
print(find([1, 2, 3, 3, 4, 5, 6]))

# 080
# xyz
# piramida
# 
# kusur