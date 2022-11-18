def rec(n: int) -> int:
    if n == 1: return 1
    return n + rec(n-1)

print(rec(3))