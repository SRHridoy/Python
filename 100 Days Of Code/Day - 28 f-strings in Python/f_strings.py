letter = "Hey my name is {} and I am from {}..."
country = "Bangladesh"
name = "Hridoy"

print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}...")


price = 49.9999
txt = f"For only {price:.2f} dollars!"
#print(txt.format(price = 49.09999))
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

#If we need to use {} we use {{}}----->
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}...")

