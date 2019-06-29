import random

keep_playing = "y"

while keep_playing != "n":
    guess = 0
    val = random.randint(1, 11)
    while guess != val:
        guess = int(input("Guess a number between 1 and 10: "))
        if val < guess:
            print("Too high! Guess again.")
        elif val > guess:
            print("Too low! Guess again.")
        else:
            print("You guessed it! You won!")
    keep_playing = input("Do you want to keep playing? (y/n): ")
