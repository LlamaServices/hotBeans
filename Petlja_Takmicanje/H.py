# Kad se zadatak unese izadje ?, ali na tabeli svacijih resenje pise 100, tako da 100 poena
n =  int(input())
l = list()
for x in range(0, n):
    nums = input().split()
    l.append(nums[0]+nums[1])

for x in l:
    print(x)