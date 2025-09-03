def cms_to_inches(inches):
    return(inches*2.54)
n = int(input("Enter the number: "))
print(f"the corresponding value in cms is {cms_to_inches(n)}")
