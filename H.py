n =  int(input())
l = list()
for x in range(0, n):
    nums = [int(x) for x in input().split()]
    l.append(nums[0]+nums[1])

for x in l:
    print(x)