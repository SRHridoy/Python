#Strings are immutable...

a = "!!!! Hridoy !!! Hridoy !!!"
print(a)
    #-->String len:
print(len(a))
    #-->String upper-lower:
print(a.upper())
print(a.lower())
    #-->Striping:
print(a.rstrip("!"))

    #-->Replace: all Occurences:
print(a.replace("Hridoy","Rahman"))

    #-->split:
print(a.split(" "))

    #-->capitalize:
blogHeading = "introduction tO pythoN"
print(blogHeading.capitalize())

    #-->center:
str1 = "Welcome to the Console!!!"
print(str1)
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

    #-->counting:
print(a.count("Hridoy"))

    #-->endswith():
str1 = "Welcome to the Console !!!"#overwrite possible in python
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

    #-->find():
str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
    #-->index():
#print(str1.index("ishh"))

    #-->isalnum():
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

    #-->isalpha():
str1 = "Welcome"
print(str1.isalpha())

    #-->islower():
str1 = "hello world"
print(str1.islower())

    #-->isprintable():
str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

    #-->isspace() :
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

    #-->istitle() :
str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

    #-->isupper() :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

    #-->startswith() :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

    #-->swapcase() :
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

    #-->title() :
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

