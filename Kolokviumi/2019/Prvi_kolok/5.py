#from time import time
def meow(num):

    def expander(num):
        if num <= 9:
            num *= 10
        if num <= 99:
            num *= 10
        if num <= 999:
            num *= 10
        return num

    count = 0
    while(num != 6174):
        l = [int(x) for x in str(num)]
        rev   = int(''.join(str(x) for x in sorted(l)))
        reved = int(''.join(str(x) for x in sorted(l, reverse=True)))
        num = reved - rev
        if num <= 999:
            num = expander(num)
        count += 1
    return count

#print('\n\n')
#start = time()
print(meow(9831))
#print(time()-start)
