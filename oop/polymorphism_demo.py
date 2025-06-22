import math
class Shape:
    def __init__(self, area):
        self.area = area
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__(area)
        self.length = length
        self.width = width
        area = length * width
class Circle(Shape):
    def __init__(self, area,radius):
        super().__init__(area)
        self.radius = radius
        area =math.pi ** 2


