def meow(d: dict, target: int) -> list:
    l = []
    for key, val in d.items():
        if val == target:
            l.append(key)
    return sorted(l)

print(meow({46:23,23:32,4:82,7:23,6:23,5:23},23))