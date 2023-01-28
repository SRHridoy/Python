class Employee:
    def __init__(self):
        self.__name = "Hridoy"

a = Employee()
#print(a.__name) #can't be accessed directly
print(a._Employee__name) #can be access indirectly
print(a.__dir__())


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())