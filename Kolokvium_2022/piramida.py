def pir(arr: list):
    for i in range(0, len(arr)):
        for x in range(0, len(arr)-1):
            arr[x] = arr[x] + arr[x+1]
        if len(arr) == 1:
            return arr[0]
        arr.pop(-1)
    return arr

# [1,2,3,4,5]
# [3,5,7,9]
# [8,12,16]
# [20,28]
# [48]

print(pir([1,2,3,4,5]))