def meow(s: str) -> str:
    dicti = {}
    maxi = 0
    maxichar = ''

    for char in s:
        if char in dicti:
            dicti[char] += 1
            counted = dicti[char]
            if counted > maxi:
                maxi = counted
                maxichar = char
        dicti.update({char:s.count(char)})
    
    return maxichar

print(meow('abbccdddafgd'))