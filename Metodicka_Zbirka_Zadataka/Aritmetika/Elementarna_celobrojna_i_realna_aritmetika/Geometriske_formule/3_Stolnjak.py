# https://petlja.org/biblioteka/r/Zbirka-python/stolnjak
# P = r**2*Pi
# O = 2rPi
# r = sqrt(P/Pi)
# O = 2*sqrt(P/Pi)*Pi
from math import pi, sqrt
povrs = float(input())
print( round(2*pi*sqrt(povrs/pi), 2) )