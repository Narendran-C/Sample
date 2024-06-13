"""
 - Single Inheritance
 - Multiple Inheritance
 - Multilevel Inheritance
 - Hierarchy Inheritance

  This inheritance can be achieved with combination of atleast two of the above-mentioned inheritance concept - Hybrid Inheritance

"""
class Dad:
    def __init__(self):
        print("Dad class Constructor")

    def phone(self):
        print("Dad's phone")


class Land():
    def __init__(self):
        print("Land class Constructor")

    def imp(self):
        print("Important Land")


class Son1(Dad, Land):
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

