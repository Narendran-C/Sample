class A:
    def __init__(self):
        super().__init__()
        print("Class A Constructor")

    def display(self):
        print("You are in Class A")


class A1():
    def __init__(self):
        super().__init__()
        print("Class A1 Constructor")

    def display(self):
        print("You are in Class A1")


class B(A, A1):
    def __init__(self):
        super().__init__()
        print("Class B Constructor")

    def display(self):
        print("You are in Class B")


obj2 = B()
