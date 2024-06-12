class Fruit:
    def __init__(self, c):
        self.color = c
        print(c)

    def show(self):
        print(self.color)


apple = Fruit("Red")

apple.show()

