# https://petlja.org/biblioteka/r/Zbirka-python/rastojanje_tacaka
from math import sqrt
x = int(input())
y = int(input())
a = int(input())
b = int(input())
r = sqrt(((x-a)**2) + ((y-b)**2))
print( '%.5f' % r )