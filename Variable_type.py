class Phone:

    chrg_type = "C-Type"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def disp(self):
        print("Brand   : " + self.brand, end=" --> ")
        print("Price   : " + self.price, end=" --> ")
        print("Charger : " + self.chrg_type)


Phone.chrg_type = "B-Type"
samsung = Phone("Samsung", "10000")
samsung.disp()

redmi = Phone("Redmi", "20000")
redmi.disp()

google = Phone("Google", "30000")
google.disp()

