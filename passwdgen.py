from string import ascii_letters
from random import seed, choice
nums = [str(x) for x in list(range(0, 10))]
seed()
passwd = ''
passwd_len = int(input("How long would you like the password to be:"))
for i in range(0, passwd_len):
    passwd += choice(choice([nums, ascii_letters]))

print(passwd)
