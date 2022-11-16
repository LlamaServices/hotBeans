from math import sqrt

def meow(osnova: int, br: int) -> int:
    if not osnova > 1:
        raise ValueError
    if not br > 0:
        raise ValueError
    lower = higher = round(sqrt(br))
    d = {
        abs(osnova**(lower-1)-br): lower-1,
        abs(osnova**(higher+1)-br): higher+1,
        abs(osnova**(lower)-br): lower 
    }
    return d.get(min(d.keys()))

print(meow(4, 12))