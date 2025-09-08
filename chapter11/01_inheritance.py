class Employee(): 
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name}. the company of the employee is {self.company}")

class programmer(Employee): 
    company = "Infotech"
    def showlanguage(self):
        print(f"the name is {self.name}. and he is good with {self.language} language.")
a = Employee()
b = programmer()
print(a.company, b.company)