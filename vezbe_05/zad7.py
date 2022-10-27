def funk(sentince):
    words = sentince.split()
    cleared_words = set()

    # clear characters that are not letters (ie '.' and ',')
    for x in words:
        word = x.lower()
        if not word[0].isalpha():
            word = word.replace(word[0], '')
        if not word[-1].isalpha():
            word = word.replace(word[-1], '')
        cleared_words.add(word)
    
    # find smallest and biggest word
    words = list(cleared_words)
    maxi = 0
    mini = float('inf')
    for index, x in enumerate(words):
        if len(x) > maxi: 
            maxi = len(x)
            index_maxi = index
        if len(x) < mini: 
            mini = len(x)
            index_mini = index

    return [words[index_mini], words[index_maxi]]

print(funk("Meow is meow, but meow is bigmeow."))