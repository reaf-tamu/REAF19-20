# Python Practice 10/16/2019
# Generate a random number between 1 and 9 inclusive. Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# Hint: remember to use the user input lessons from the very first exercise.
#  - Keep the game going until the user types "exit"
#  - Keep track of how many guesses the user has taken, and when the game ends, print counter.

import random
guesses = 1

print("-----Guessing Game-----")
print("How to Play: Guess a number between 1 and 9, inclusive. If you guess right, you win!")
randomNum = random.randint(1, 10)

while True:
    guess = int(input("Your guess: ").strip())
    if guess == randomNum:
        print(guess, "is correct! You won using", guesses, "guesses.")
        exit()
    else:
        guesses += 1
        if guess < randomNum:
            print("Too low. Guess higher!")
        else:
            print("Too high. Guess lower!")
