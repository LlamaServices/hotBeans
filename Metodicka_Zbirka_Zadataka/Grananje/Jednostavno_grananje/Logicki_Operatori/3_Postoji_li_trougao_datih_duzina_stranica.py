# https://petlja.org/biblioteka/r/Zbirka-python/postoji_li_trougao_datih_duzina_stranica

a = float(input())
b = float(input())
c = float(input())

if a < b + c and b < a + c and c < a + b:
    print("da")
else:
    print("ne")