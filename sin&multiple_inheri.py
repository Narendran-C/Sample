"""
Has one Base Class( Dad ) and one derived class( Son ) - Single Inheritance

Has two Base Class( Dad, Mom ) and one derived Class( Son ) - Multiple Inheritance

"""

class Dad:
    def __init__(self):
        print("Dad class constructor")

    def phone(self):
        print("Dad's phone")


class Mom:
    def __init__(self):
        print("Mom class constructor")

    def sweet(self):
        print("Mom's sweet")


class Son(Dad, Mom):
    def __init__(self):
        print("Son class constructor")

    def laptop(self):
        print("Son's Laptop")


ram = Son()




