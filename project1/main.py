import random
'''
snake = 1
water = -1
gun = 0
'''
computer = random.choice([0, 1, -1])
yourstrg = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake", -1:"water", 0:"Gun"}

you = yourDict[yourstrg]

if (computer == you):
    print("It is draw")

else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You win")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win")
