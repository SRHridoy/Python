class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.1416 * super().area()
    

rec = Shape(3, 5)
print(rec.area())

cir = Circle(5)
print(cir.area())