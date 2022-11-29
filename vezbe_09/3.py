def meow(d: dict, target: int) -> list:
    l = []
    for key in d:
        if d.get(key) == target:
            l.append(key)
    return sorted(l)

print(meow({8:50,2:50,3:40,7:50,1:50}, 50))