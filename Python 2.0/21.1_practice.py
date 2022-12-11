name = input("Enter Your name : ")

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Namme must be a maximum of 50 characters.")
else:
    print("Name looks good!")


