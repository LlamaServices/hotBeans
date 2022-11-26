def meow(num):
    l = [int(x) for x in str(num)]
    s = set()
    string = ''

    prethodni = l[0]
    string += str(prethodni)

    for x in l:
        if x != prethodni:
            string += str(x)
            prethodni = x

    return string


#print(meow(1223334556))
print(meow(input()))