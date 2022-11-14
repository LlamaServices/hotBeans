# https://petlja.org/biblioteka/r/Zbirka-python/prestupna_godina

def div(num, divider):
    return True if num % divider == 0 else False

x = int(input())

if (div(x, 4) and  not div(x, 100)) or div(x, 400): print('da')
else: print('ne')