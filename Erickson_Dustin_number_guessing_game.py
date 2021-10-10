# Dustin Erickson
# 10-9-2021
#I created a number guessing game in a function. It creates a random number, then asks the user for an input. It then calculates if the number
# is high or low. It then allows the user to continue to guess. Once the input matches the random number, it ends the function. I then created
# a main function that calls the guessing game function. Then I called the main function.

import random           #Imports the random module

def guessing_game():        #defines the guessing game function
    num = random.randint(0,100)         #Creates a random integer from 0 to 100
    truth = False           #Sets the initial value for if the guess is correct to false because the guess has not been made
    guess = int(input("Guess the numeber: "))   #Asks the user for a guess
    while truth == False:           #Initiates the loop
        if guess < num:             #If the guess is to low it prints too low, and lets the user reguess
            print("Too Low")
            guess = int(input("Guess the numeber: "))
        elif guess > num:           #If the number is to high it prints too high, and lets the user reguess
            print("Too High")
            guess = int(input("Guess the numeber: "))
        else:
            print("Just right")     #If the guess is correct, it ends the loop and prints "just right"
            truth == True
            break


def main():             #Creates a main loop because the instructions ask for it. I am not sure if this is what you meant.
    guessing_game()     #Calls the guessing game function

main()          #Calls the main function
