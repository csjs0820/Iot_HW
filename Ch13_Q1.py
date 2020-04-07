PI = 3.141592

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def calcPerimeter(self):
        self.perimeter = 2 * PI * self.radius
    def calcArea(self):
        self.area = PI * self.radius * self.radius
    def __str__(self):
        msg = "반지름:"+ str(self.radius)+ " 둘레:"+ str(self.perimeter)+ " 면적:"+ str(self.area)
        return msg

mycircle = Circle(100)
mycircle.calcPerimeter()
mycircle.calcArea()
print(mycircle)
