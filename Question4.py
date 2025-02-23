class shape:
    def __init__(self):
        return 0
class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width
    def get_area(self):
        return self.area
class Circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.area =  (22/7)* (self.radius ** 2)
    def get_area(self):
        return self.area
rectangle1 = Rectangle(5, 10)
circle1 = Circle(5)
print(rectangle1.get_area())  
print(circle1.get_area())  
