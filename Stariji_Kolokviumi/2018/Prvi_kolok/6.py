def whothefuckknows(arr: list) -> int | None:
    d = {}
    for x in arr:
        count = arr.count(x)
        if count % 2 != 0:
            # d = {number : number of appearences}
            d.update({count: x})

    find = max(d.values())
    if find:
        return find
    else:
        return None

print(whothefuckknows([3, 9, 5, 3, 5, 3]))