# https://petlja.org/biblioteka/r/Zbirka-python/radno_vreme
s = int(input())
m = int(input())

poslato = m + s*60
pocetak = 9*60
kraj = 17*60

if poslato >= pocetak and poslato < kraj:
    print('da')
else: print('ne')