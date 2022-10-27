def funk(niz): return sum([1 for x in niz if '5' in str(x)])

print(funk([123, 342, 256, 23456, 342, 4324, 3564]))