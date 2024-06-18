class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        l = 10
        b = 20
        return l * b


obj1 = Rectangle()
print(obj1.area())
