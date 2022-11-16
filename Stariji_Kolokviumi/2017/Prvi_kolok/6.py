def meow(string: str):
    sum = 0
    for x in string:
        if x.isnumeric():
            sum += int(x)
    if sum == 0:
        raise ValueError
    return sum

print(meow("а<37д5е:B!"))