# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


""" ----------LET'S DO IT---------- """

""" ----------random letter generator---------- """
import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

""" ----------Driver Program---------- """

choice = str(input("Write Encode to make your message Secreat or Decode to retrive your message from Secreat message: "))

""" ----------ENCODING---------- """
if(choice.lower() == "encode"):
    message = str(input("Write your message to encode it : "))

    preString = get_random_string(3);
    postString = get_random_string(3);

    if(len(message)<3):
    #There is no inbuilt function for reversing a string
        message = message[::-1]
    else:
        firstLetter = message[0]
        message = message[1:len(message)]
        message = preString+message+firstLetter+postString
    print("Your Encoded Secreat Message is : ", message)

else:
    """ ----------DECODING---------- """
    secreat_message = str(input("Write your message to decode it : "))
    if(len(secreat_message)<3):
        print("Your Secreat Message is : ", secreat_message[::-1])
    else:
        secreat_message = secreat_message[3:-3]
        lastLetter = secreat_message[len(secreat_message)-1]
        secreat_message = secreat_message[:len(secreat_message)-1]
        secreat_message = lastLetter + secreat_message;
        print("Your Real Message is : ",secreat_message)






