"""

Number guessing game 
written by Mikyas Mulugeta.

"""
import random

com_num = random.randint(1, 101)


while True:

   # Request a guess from the user
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > com_num:
            print("Too high!")
        elif guess < com_num:
            print("Too low!")
        elif guess == com_num:
            print("Congratulations! You guessed the number. ")
            break
        
    except ValueError:
        print("Please enter a valid number")