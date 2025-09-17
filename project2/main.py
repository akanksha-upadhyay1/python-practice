import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    guesses = guesses + 1
    a = int(input("guess the number: "))
    if(a>n):
        print("lower number please")
    else:
        print("higher number please")
print(f"You have guessed the number {n} correctly in {guesses} attempts")