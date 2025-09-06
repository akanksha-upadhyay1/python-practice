class Employee:
    language = "py" #This is class attribute.
    salary = 1200000
    
    #def getInfo(self):
        #print(f"the language is {self.language}. the salary is {self.salary}.")
    
    def __init__(self, name, salary, language): #dunder method is a method which is automatically called
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    # @staticmethod
    # def greet():
    #     print("Good afternoon")

ritik = Employee("saurav", 1300000, "java")
#ritik.language = "javascript"
#ritik.name = "Ritik" #this is instance attribute
print(ritik.name, ritik.salary, ritik.language)

 