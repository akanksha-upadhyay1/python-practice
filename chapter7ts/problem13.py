'''
***
* *
***
'''

n = int(input("Enter the number: "))
for i in range(1, n+1): # i = rows
    # for j in range(1, n+1): # j = column
    if(i==1 or i==n):
        print("* "*n)
    else:
        print("*", end="")
        print(" "*(2*n-3), end="")
        print("*")

  