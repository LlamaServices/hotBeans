# https://petlja.org/biblioteka/r/Zbirka-python/razmaknute_dijagonale
x, y = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
if (x + y - 1) % 3 == 0: print('crno')
else: print('belo')
if (a + b - 1) % 3 == 0: print('crno')
else: print('belo')
if (c + d - 1) % 3 == 0: print('crno')
else: print('belo')