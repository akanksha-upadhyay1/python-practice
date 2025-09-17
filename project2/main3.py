import random
n = random.randint(1, 100)
a = -1
guesses = 0
wrong_streak = 0
correct_streak = 0 

while a != n:
    a = int(input("Guess the number: "))
    guesses += 1

    if a > n:
        print("Lower number please.")
        wrong_streak += 1
        correct_streak +=1

    elif a < n:
        print("Higher number please.")
        wrong_streak += 1
        correct_streak += 1

    # if a == n:
    #     # Yahan par kuch nahi likh rahe, loop condition hi rokega (a != n)
    #     pass

    if wrong_streak == 5:
        print("Tum gadhe ho!")
        wrong_streak = 0  # Fir se count shuru karo

print(f"You guessed the number {n} correctly in {guesses} attempts.")

if correct_streak <= 5:
    print("you are excellent")