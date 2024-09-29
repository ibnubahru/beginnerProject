"""
Rock paper scissors game 
written by Mikyas Mulugeta 

"""
import random

while True:
    choices =('r', 'p', 's')
    user_choice = input("Rock, paper or scissors? (R/P/S): ").lower()
    comp_choice = random.choice(choices)


    def checkResult():
        print(f"you chose {user_choice}")
        print(f"computer chose {comp_choice}")
        print("you win!")

    if user_choice not in choices:
        print("Invalid input")
    elif user_choice == "r" and comp_choice == "s":
        checkResult()
    elif user_choice == "p" and comp_choice == "r":
        checkResult()
    elif user_choice == "s" and comp_choice == "p":
        checkResult()
    else:
        print("Computer wins!")
    
    repeat_game = input("Do you want to coninue? y/n").lower()
    if repeat_game == "n":
        print("good to see you")
        break
    elif repeat_game == "y":
        continue