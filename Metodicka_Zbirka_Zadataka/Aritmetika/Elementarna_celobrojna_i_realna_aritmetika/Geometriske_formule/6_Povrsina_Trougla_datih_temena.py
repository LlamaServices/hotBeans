# https://petlja.org/biblioteka/r/Zbirka-python/povrsina_trougla_datih_temena
ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())

print( format(abs(( ax*(by-cy) + bx*(cy-ay) + cx*(ay-by) )*(.5)), '.5f') )