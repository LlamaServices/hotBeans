def funk(s):
    s1 = set()
    s2 = set()
    for c in s:
        if c in s1:
            s2.add(c)
        else:
            s1.add(c)
    return s2

print(funk("abbccd"))