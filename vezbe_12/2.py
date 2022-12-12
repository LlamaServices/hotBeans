'''
Написати функцију која транспонује дату квадратну матрицу.
'''
def meow(arr: list) -> list:
    n = len(arr[0])
    for i in range(n):
        c = i + 1
        while c < n:
            arr[i][c], arr[c][i] = arr[c][i], arr[i][c]
            c += 1

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

meow(arr)

for x in arr:
    print(x)