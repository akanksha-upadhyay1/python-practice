class Programmer: 
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("akanksha", 1200000, 160021)
print(p.name,p.company,p.salary,p.pin)
r = Programmer("rohan", 1200000, 160021)
print(r.name,r.company,r.salary,r.pin)