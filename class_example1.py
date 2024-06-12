class Student:
    def __init__(self):
        self.name = "karthi"
        self.reg_no = 3564

    def display(self):
        print("Name            : ", self.name)
        print("Register Number : ", self.reg_no)


s1 = Student()
s2 = Student()

s1.name = "Naren"
s1.reg_no = 1001
s2.name = "pavi"
s2.reg_no = 1002

s1.display()
s2.display()

