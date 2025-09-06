class Employee:
    language = "py" #This is class attribute.
    salary = 1200000

ritik = Employee()
ritik.name = "Ritik" #this is instance attribute
print(ritik.name, ritik.language, ritik.salary)

akanksha = Employee()
akanksha.name = "Akanksha"
print(akanksha.name, akanksha.language, akanksha.salary)

# Here name is instance attribute and language and salary are class attribute because they are directly belong to the class



