def intertwine(s1, s2):
    s3 = ''
    flag = True

    while s1 and s2:
        if flag:
            s3 += s1[0]
            s1 = s1[1:]
        if not flag:
            s3 += s2[0]
            s2 = s2[1:]
        flag = not flag

    return s3 + s1 + s2

print(intertwine("Владимир","Миловановић"))