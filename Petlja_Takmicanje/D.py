# 100 Poena
instr = input()
outstr = ''

last = instr[0]
outstr += last
if instr.count(last) > 1:
    outstr += str(instr.count(last))

for x in instr:
    if x != last:
        outstr += x
        if instr.count(x) > 1:
            outstr += str(instr.count(x))
        last = x

print(outstr)