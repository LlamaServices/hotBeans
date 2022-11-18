def rec(vrs, kol):
    if kol == 1: return 1
    if vrs == kol: return 1
    return rec(vrs-1, kol) + rec(vrs-1, kol-1)

print(rec(3, 2))