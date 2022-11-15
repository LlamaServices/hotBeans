def meow(n):
    sum = 0
    for x in range(n, 0, -1):
        sum+= (x-2)*5 + 5
    return sum+1

print(meow(6))