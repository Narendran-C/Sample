class Laptop:
    chrg_type = "C-Type"

    def __init__(self):
        self.brand = ""
        self.price = 15

    def set_price(self, price):
        self.price = price

    def get_price(self):
        print(self.price)

    @classmethod
    def change_chrg_type(cls):
        cls.chrg_type = "A-Type"
        print("Charger type changed to A-Type")

    @staticmethod
    def info():
        print("This is Laptop class method")


hp = Laptop()
hp.set_price(20001)
hp.get_price()

Laptop.change_chrg_type()

dell = Laptop()
print(dell.chrg_type)

hp.info()
