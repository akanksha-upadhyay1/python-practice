class Employee():
    def __init__(self):
        
        print("Constructor of Employee")
    a = 1
class programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")
    b = 2
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c = 3
     
# o = Employee()
# print(o.a) # print the a attribute

o = manager()
# print(o.a, o.b, o.c) 

# o = programmer()
