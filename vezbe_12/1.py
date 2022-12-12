def meow(arr: list) -> int:
    sum = 0
    for i in range(len(arr[0])): sum += arr[i][i]
    return sum
    #return sum([arr[i][i] for i in range(len(arr[0]))])


arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(meow(arr))