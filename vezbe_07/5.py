def rec(s):
    if not s: return s
    return rec(s[1:]) + s[0]

print(rec('aleksa'))