def rec(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return rec(s[1:-1])

print(rec('racecar'))