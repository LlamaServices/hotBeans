'''
{1:10, 2:20, 3:30} -> {10: [1], 20: [2], 30: [3]}
{1:10, 2:20, 3:30, 4:30} -> {10: [1], 20: [2], 30: [3, 4]}
{4:True, 0:True, 2:True} -> True: [0, 2, 4]
'''
def meow(d: dict) -> dict:
    d1 = {}
    for value in d.values():
        if not value in d1:
            d1.update({value:sorted([k for k in d if d[k] == value])})
    return d1

print(meow({1:10, 2:20, 3:30, 4:30}))