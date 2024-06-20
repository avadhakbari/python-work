#24. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

c = Circle(5)

print("area of circle is :", c.area())
print("perimeter of circle is :", c.perimeter())