import random2 as rn

letters = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
sym = '`~!@#$%^&*()_+[]{-=}\|;":,./<>?'

total = letters+letters.upper()+nums+sym


def generator(length):
    passwd = ''
    for i in range(0, length):
        passwd += rn.choice(total)
    return passwd

print("Hello World!")
print(generator(16))
