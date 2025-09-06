class Employee:
    language = "py" #This is class attribute.
    salary = 1200000
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}.")
    
    def _init_(self): #dunder method is a method which is automatically called
        print("I am creating an object")
    @staticmethod
    def greet():
        print("Good afternoon")

ritik = Employee()
ritik.language = "javascript"
ritik.name = "Ritik" #this is instance attribute
print(ritik.name, ritik.language, ritik.salary)
ritik.getInfo()
ritik.greet()