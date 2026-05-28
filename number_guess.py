import random

print("Welcome to the Number Guessing game!")
print("You get 6 attempts to guess a random number from 1-100")

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 6
won = False

while attempts < 6:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print("Congratulations! ", str(secret_number), " is the correct number!")
        won = True
        break
    elif guess < secret_number:
        print("Oof, not quite. Try higher.")
    else:
        print("Oof, not quite. Try lower.")

if won == False:
    print("You are out of attempts! Better luck next time!")