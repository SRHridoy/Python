def average(a=9,b=1):
    print("The averaga is ",(a+b)/2)

#average(4,6)
#average(1,5)
#average(5)
average(b=9)
average(b=9,a=21)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy","Agarwal","Jain")

# def name(fname, mname, lname):------>ERROR
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")


#Tuple as parameter------------->
""" def avg(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ",sum/len(numbers))
avg(5,6,7,1) """

#---------->Pore...Dictionary----->
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

def avg(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #return 7
    return sum / len(numbers)

ans = avg(5,6,7,1)
print(ans)

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")