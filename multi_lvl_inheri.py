"""
In this case, the base class of a derived class itself a derived class of a Base class - Multiple Level Inheritance

          Grandpa Class
                 \
              Father Class
                   \
              GrandSon (or) Son

"""
class Grandpa:
    def __init__(self):
        print("Grandpa class constructor")

    def phone(self):
        print("Grandpa's phone")


class Dad(Grandpa):
    def __init__(self):
        print("Dad class constructor")

    def money(self):
        print("Dad's money")


class Son(Dad):

    def __init__(self):
        print("Son class constructor")

    def laptop(self):
        print("Son's laptop")


dad = Dad()
dad.money()
dad.phone()

