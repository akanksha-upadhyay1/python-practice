class Employee:
    language = "py" #This is class attribute.
    salary = 1200000

ritik = Employee()
ritik.language = "javascript"
ritik.name = "Ritik" #this is instance attribute
print(ritik.name, ritik.language, ritik.salary)

akanksha = Employee()
akanksha.name = "Akanksha"
print(akanksha.name, akanksha.language, akanksha.salary)
