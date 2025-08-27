a = int(input("Enter your age: "))
# If statement no. 1 
if(a%2 == 0):
    print("a is even")
# If statement no. 2 
if(a>=18):
    print("you are above the age of consent")
elif(a<0):
    print("you are giving wrong age")
elif(a==0):
    print("you are giving invalid age")
else:
    print("you are below the consent")

print("end the program")