# https://petlja.org/biblioteka/r/Zbirka-python/kucni_red

time = int(input())

if time < 6 or (time >= 13 and time < 17) or time >= 22:
    print('ne moze')
else: print('moze')