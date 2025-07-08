# Task 2: Number Guessing Game

import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess == number:
            print(f"Correct! You guessed it in {attempts} tries.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

guess_game()
