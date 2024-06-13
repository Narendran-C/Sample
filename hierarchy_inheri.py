"""
Has one Base Class( Dad ) and two or more  derived class( Son1, Son2, Son3 ) - Hierarchy Inheritance

"""

class Dad:
    def __init__(self):
        print("Dad class Constructor")

    def phone(self):
        print("Dad's phone")


class Son1(Dad):
    def __init__(self):
        print ("Son1 class Constructor")


class Son2(Dad):
    def __init__(self):
        print("Son2 class Constructor")


class Son3(Dad):
    def __init__(self):
        print("Son3 class Constructor")


son1 = Son1()
son2 = Son2()
son3 = Son3()
son1.phone()
son2.phone()
son3.phone()

