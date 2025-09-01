# find factorial by "for" loop
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*n
    n = n-1
print("factorial: ", fact)