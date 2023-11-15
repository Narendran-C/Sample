import module_method as mm


class Simple:
    x = 10

    @staticmethod
    def display():
        print('Calling static method :', Simple.x)


Simple.display()
mm.func()
