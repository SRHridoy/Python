# import time
# name = input("Enter Your name : ").title()
# currentTime = time.strftime('%H:%M:%S')
# h = int(time.strftime('%H'))
# if(h<12):
#     print("Good Morning,",name)
# elif(h>12 and h<17):
#     print("Good Afternon,",name)
# else:
#     print("Good Night,",name)

import time

name = input("Enter Your Name : ").title()
currentTime = time.strftime("%I:%M")
date = time.strftime("%d/%m/%y")
h = int(time.strftime("%H"))
if(h<12):
    print("Good Morning, ", name)
elif(h>12 and h < 17):
    print("Good Afternoon ", name)
else:
    print("Good Night ",name)

weekDay = time.strftime("%A")
monthName = time.strftime("%B")

print("The DATE is :", date)
print("Current Time is : ", currentTime)
print("Today is ",weekDay)
print("This is ",monthName , " month")
