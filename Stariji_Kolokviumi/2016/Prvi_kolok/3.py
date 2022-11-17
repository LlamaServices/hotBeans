def invertor(arr: list) -> list:
    for x in arr:
        x.reverse()
    arr.reverse()
    return arr

print(invertor([[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]))