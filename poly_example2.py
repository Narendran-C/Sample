class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Bird(Animal):
    def sound(self):
        print("Birds sing")


animal = Animal()
dog = Dog()
bird = Bird()

animal.sound()
dog.sound()
bird.sound()
