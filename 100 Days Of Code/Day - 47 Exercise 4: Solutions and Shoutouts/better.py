import string
import random


def code_word(user1, key):
    b = user1.split()
    lst = []
    for i in b:
        if (len(i) < 3):
            a = i[::-1]
            lst.append(a)
        else:
            code = i[1:]+i[0]
            code1 = ''.join(random.choices(string.ascii_lowercase, k=key)) + \
                code + ''.join(random.choices(string.ascii_lowercase, k=key))
            lst.append(code1)
    a = ' '.join(lst)
    return a


def dcode_word(user, key):
    b = user.split()
    lst = []
    for i in b:
        if (len(i) < 3):
            code = i[::-1]
            lst.append(code)
        else:
            code2 = i[key:-key]
            try:
                code1 = code2[-1]+code2[0:-1]
            except IndexError:
                print('Your encryption key is greater than message:')
            lst.append(code1)
    a = ' '.join(lst)
    return a


while True:
    u = input('Enter Code or Decode or Quit:')
    if (u.lower() == "code"):
        user1 = input('Enter your message:')
        try:
            user2 = int(input('Enter your key as (3 or 4 or 6):'))
        except Exception as e:
            pass
        try:
            print(code_word(user1, user2))
        except Exception as e:
            print('Please enter only Digits for encryption:')
    elif (u.lower() == "decode"):
        user1 = input('Enter Your message:')
        try:
            key = int(input('Enter your key for Dcrypting:'))
            if (key > len(user1)):
                print('Your Decryption key is greater than message:')
            else:
                print(dcode_word(user1, key))
        except Exception as e:
            print('Please enter only Digits for Decryption:')
    elif (u.lower() == 'quit'):
        break
    else:
        print('Please enter vaild detail:')
