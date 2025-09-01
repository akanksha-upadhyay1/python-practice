# reversed the number
n = int(input("Enter the number: "))
rev = 0
while n > 0:
    digit = n % 10 # it will give remainder
    rev = rev*10 + digit # rev no
    n = n // 10 # next number without decimal
print("reversed number: ", rev)
