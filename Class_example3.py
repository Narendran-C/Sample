class Teacher:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def show(self):
        print("Name : ", self.name)
        print("Regno : ", self.reg_no)


t1 = Teacher("Ramesh", "1")
t2 = Teacher("Suresh", "10")
t1.show()
t2.show()
