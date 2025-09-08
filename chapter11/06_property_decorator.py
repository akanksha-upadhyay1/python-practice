class Employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")

    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
e.name = "akanksha upadhyay"
print(e.fname, e.lname)



e.show()