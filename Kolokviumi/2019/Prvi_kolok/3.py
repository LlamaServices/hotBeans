def meow(niz):
    repeated = []
    seen = set()
    for x in niz:
        if x in seen: repeated.append(x)
        seen.add(x) 
    return sorted(list(set(repeated)))

print(meow([1,2,3,2,1,5,6,5,5,5]))