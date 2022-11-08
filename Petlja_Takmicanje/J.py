# 100 poena
from time import time as t
def meow(num):
    def sumDig(num):
        return sum([int(x)**2 for x in str(num)])

    starting_num = num
    c = 0
    while(True):
        num = sumDig(num)
        if num == starting_num: return 'ne'
        if num == 1: return 'da'
        c += 1
        if c > 100: return 'ne'

print(meow(int(input())))