# 100 poena
keyboard = list(input())
word = input()
time = 0
for x in range(0, len(word)-1):
    space = abs(keyboard.index(word[x]) - keyboard.index(word[x+1]))
    time += space

print(time)