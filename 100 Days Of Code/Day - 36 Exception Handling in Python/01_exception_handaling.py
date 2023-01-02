""" a = input("Enter the number: ")
print(f"Multiplication tale of {a} is : ")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
# except Exception as e:
except:
    print("INVALID INPUT!")

print("Some Important lines of Code")
print("End of Program") """


""" ----------MULTIPLE ERROR HANDALING---------- """
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
