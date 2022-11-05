# 100 poena
from time import time as t
def meow(num):
    def sumDig(num):
        suma = 0
        while(num>0):
            suma += (num%10)**2
            num //=10
        return suma

    starting_num = num
    c = 0
    while(True):
        num = sumDig(num)
        if num == starting_num: return 'ne'
        if num == 1: return 'da'
        c += 1
        if c > 100: return 'ne'

print(meow(int(input())))