a = int(input("enter a number: "))
b = int(input("enter the second number: "))

if(b == 0): 
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"the devision a/b is {a/b}")

