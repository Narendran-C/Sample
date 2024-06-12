class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        print("Addition of the 2 number is   : ", (a + b))

    def sub(self):
        print("Difference of the 2 number is :", (self.a - self.b))

    def mul(self):
        print("Product of the 2 number is    : ", (self.a * self.b))

    def div(self):
        print("Division of the 2 number is   : ", (self.a / self.b))


obj1 = Calculator(2, 3)
obj1.add(3, 3)
obj1.sub()
obj1.mul()
obj1.div()
