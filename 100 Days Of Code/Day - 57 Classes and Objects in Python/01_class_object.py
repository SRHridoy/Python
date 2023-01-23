class Person:
    name = "Hridoy"
    occupation = "Software Devloper"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}" )

a = Person()

a.name = "Shuvo"
a.occupation = "Accountant"

# print(a.name, a.occupation)
a.info()