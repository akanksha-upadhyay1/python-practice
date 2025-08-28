marks1 = int(input("Enter the marks a1: "))
marks2 = int(input("Enter the marks a2: "))
marks3 = int(input("Enter the marks a3: "))
# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3):
    print("you have passed the exam:", total_percentage)
else:
    print("try another time")