import math
class Shape():
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
    def toString(self):
        return f"A Shape with colors of {self.color} and {self.filled}"
shape1 = Shape('red',True)
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return 3.14*(self.radius**2)
    def getPerimeter(self):
        return (3.14 * self.radius)/2
    def toString(self,obj):
        return f"A Circle with radius={self.radius}, which is a subclass of {obj.toString()}"
class Rectangle(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def getArea(self):
        return self.width*self.length
    def getPerimeter(self):
        return (self.width+self.length)*2
    def toString(self,obj):
        return  f"A Rectangle with width={self.width} and length={self.length}, which is a subclass of {obj.toString()}"
circle1 = Circle(5)
rect1 = Rectangle(5,10)

class Square(Rectangle):
      def getAreaOfSquare(self):
          return f'its a subclass with {self.length} and {self.width}'

print(circle1.toString(shape1))
print(rect1.toString(shape1))
square1 = Square(2,3)
print(square1.getAreaOfSquare())