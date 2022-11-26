def zic(br):
    mirrored = [0, 8]
    
    digits = [int(x) for x in br]

    # da li imaju neke cifre koje nisu 0 ili 8
    for x in digits:
        if x not in mirrored:
            return 'NE'
    
    # da li su sve cifre 0
    truth = []
    for x in digits:
        if x == 0:
            truth.append(True)
        else:
            truth.append(False)
    if all(truth):
        return 'DA'
    
    digits = list(reversed(digits))

    if digits[0] == 0:
        return 'NE'
    return 'DA'


# print(zic(input()))
print('123: ', zic('123'))
print('800: ', zic('800'))
print('008: ', zic('008'))
print('808: ', zic('808'))
print('080: ', zic('080'))
print('0000: ', zic('0000'))