# 60 poena
def meow(n):
    def check(num):
        prev = num % 10
        num //= 10
        if num % 10 > prev:
            return False
        while num > 0:
            if num % 10 > prev:
                return False
            prev = num % 10
            num //= 10
        return True
    
    if check(n):
        return n

    lower = higher = n
    x,y = check(lower), check(higher)
    while not (x or y):
        lower -= 1
        higher += 1
        x,y = check(lower), check(higher)
    
    sol = ''
    if check(lower): sol += str(lower)
    if check(higher):
        if sol:
            sol+= ' ' + str(higher)
        else:
            sol = str(higher)

    return sol


print(meow(int(input())))