#from time import sleep
def meow(l: list) -> dict:
    d = {}

    l = sorted(list(set(l)), key = len)
    #print(l)

    x = 0
    lenght = len(l[x])

    while x < len(l):
        values = [y for y in l if len(y) == lenght]
        #print('values: ', values)
        if values:
            d.update( { len(l[x]): values } )
            #print('d: ', d)

            x += len(values)
            #print('x: ', x)
            try:
                lenght = len(l[x])
            except:
                break
            #sleep(2)
        if not values:
            x += 1
            lenght += x

    return d
    
print(meow('Ja smatram da je ovo resenje konceptivno veoma retardirano'.split()))