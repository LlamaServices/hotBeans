# https://petlja.org/biblioteka/r/Zbirka-python/zbir_godina_brace_i_sestre
# n = 3a + a + 3
# n = 4a + 3
# 4a = n - 3
# a = (n - 3) / 4

if (int(input()) - 3) % 4 == 0:
    print('da')
else: print('ne')