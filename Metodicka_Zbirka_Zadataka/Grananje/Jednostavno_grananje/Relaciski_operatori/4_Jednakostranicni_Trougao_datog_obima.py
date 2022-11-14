# https://petlja.org/biblioteka/r/Zbirka-python/jednakostranicni_trougao_datog_obima
a = int(input())
b = int(input())
c = int(input())

if (a+b+c) % 3 == 0: print('da', (a+b+c)//3)
else: print('ne')