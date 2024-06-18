"""
Encapsulation can be achieved by Access Specifiers
 1. Public Access Specifiers - Can be accessed outside and inside the class
 2. Private Access Specifiers - Can be accessed only within the class
 3. Protected Access Specifiers - can be accessed outside and inside the class
"""
class Company:
    def __init__(self):
        self._companyName = "Google"

    def display(self):
        print(self._companyName)

class Derived(Company):
    pass


d1=Derived()
c1 = Company()
#c1.display()
print(d1._companyName)



