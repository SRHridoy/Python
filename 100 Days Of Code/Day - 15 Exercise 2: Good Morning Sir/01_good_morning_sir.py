import time
name = input("Enter Your name : ").title()
currentTime = time.strftime('%H:%M:%S')
h = int(time.strftime('%H'))
if(h<12):
    print("Good Morning,",name)
elif(h>12 and h<17):
    print("Good Afternon,",name)
else:
    print("Good Night,",name)
