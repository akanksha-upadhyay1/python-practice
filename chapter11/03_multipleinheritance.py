class Employee(): 
    company = "ITC"
    name = "akanksha"
    def show(self):
        print(f"the name of the employee is {self.name}. the company of the employee is {self.company}")

class coder():
    language = "python"
    def printlanguage(self):
        print(f"out of all languages here is your language: {self.language}")


class programmer(Employee, coder): 
    company = "Infotech"
    def showlanguage(self):
        print(f"the name is {self.company}. and he is good with {self.language} language.")
a = Employee()
b = programmer()
print(a.company, b.company)
b.show()
b.printlanguage()
b.showlanguage()