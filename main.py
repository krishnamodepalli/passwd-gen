import random as rn

letters = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
sym = '`~!@#$%^&*()_+[]{-=}\|;":,./<>?'

total = letters+letters.upper()+nums+sym


def generator(length):
    passwd = ''
    for i in range(0, length):
        passwd += rn.choice(total)
    return passwd


if __name__ == "__main__":
    print(generator(16))
