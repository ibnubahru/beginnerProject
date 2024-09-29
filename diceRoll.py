"""
 Dice rolling game
 simple python console program
 written by Mikyas Mulugeta 

"""
import random

while True: 
    # Request the User for input
    choice = input('Roll the dice? (y/n): ')
    choice = choice.lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print(f"{die1}, {die2}")

    elif choice == 'n':
        print("Thanks for playing!")
        break        
    else: 
        print("Invalid choice, Please enter either 'y' or 'n' ")
        