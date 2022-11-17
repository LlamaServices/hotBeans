# 92 poena
def meow(arr: list) -> int:
    if len(set(arr)) == 1:
        return 1
    
    NAJduz = 1
    duz = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            duz += 1
        
        if arr[i] > arr[i-1] and duz > NAJduz:
            NAJduz = duz
            duz = 1

        if arr[i] > arr[i-1] and not duz > NAJduz:
            duz = 1

        if i == (len(arr) - 1):
            if duz > NAJduz:
                NAJduz = duz

    return NAJduz

#print(meow([int(x) for x in input().split()]))
print(meow( [2,2,2,2,1] ))