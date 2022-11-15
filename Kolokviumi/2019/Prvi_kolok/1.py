def najReci(input_string):

    strList = input_string.split()
    strList_cleaned = []

    for string in strList:
        if not string[0].isalpha():
            string = string[1:]
        if not string[-1].isalpha():
            string = string[:-1]
        strList_cleaned.append(string)

    strList_cleaned.sort(key=len)

    return strList_cleaned[0], strList_cleaned[-1]

print(najReci('Covek je rodjen da radi, da trpi i da se bori, ko tako ne cini, mora propasti. -Nikola Tesla'))

