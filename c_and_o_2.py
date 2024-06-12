class Laptop:
    def __init__(self):
        self.ram = ""
        self.proc = ""

    def display(self):
        print("RAM       :", self.ram)
        print("Processor :", self.proc)


hp = Laptop()
hp.ram = "8GB"
hp.proc = "i5"
hp.display()
