import random

number_to_guess = random.randint(1,10)
guess = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while guess != number_to_guess:
    guess = int(input("Enter your guess number: "))
    if guess < number_to_guess:
        print("Too low my friend!")
    elif guess > number_to_guess:
        print("Too hight my friend!")

print("Congratulations! You guessed it!")