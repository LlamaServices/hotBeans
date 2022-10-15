# Ovo resenje je ocajno napisano, bolela me je glava kad sam ga pisao tako da
# *Ne gledajte ovo, vec D2*
# 48 poena 

instr = input()
outstr = ''
last = ''
if instr[0] == instr[-1]:
    print(instr[0] + str(instr.count(instr[0])))
else:
    instr = list(instr)
    while len(instr):
        if instr[0] == instr[-1]:
            outstr += instr[0]
            if instr.count(instr[0]) > 1:
                outstr += str(instr.count(instr[0]))
            break
        c = instr[0]
        outstr += c
        if instr.count(c) > 1:
            outstr += str(instr.count(c))
        for x in instr:
            try:
                instr.remove(c)
            except:
                pass

print(outstr)