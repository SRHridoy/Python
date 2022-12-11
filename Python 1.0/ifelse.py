age = input("What is Your age?")

if int(age) >= 18:
    print("You are an adult")
    print("You can Vote")
elif 18 > int(age) > 3:
    print("You are in School")
else:
    print("You are a Child")


print("Thank You")
