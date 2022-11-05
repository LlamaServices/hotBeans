# 100 poena
from math import sqrt

def prost(br):
    if br > 1:
        for i in range(2, int(sqrt(br))+1):
            if br % i == 0:
                return False
        return True
    else: return False

def find(num):
    if prost(num):
        print(num)
        return
    lower = higher = num
    while not (prost(lower) or prost(higher)):
        lower -= 1
        higher += 1
    if prost(lower): print(lower)
    if prost(higher): print(higher)
    return

num = int(input())
find(num)
