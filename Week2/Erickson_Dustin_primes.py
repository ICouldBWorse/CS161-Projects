# Dustin Erickson
# 10-9-2021
# This program imports the math module, asks for an input number, verifies the input is a number, tests if its a prime using a function,
# and then prints the result. I tested for primality for all numbers between two and the square root of the input because all factors after
# the square root are just mirrors of previous factors. I added 1 to the square root to account for the numbers less than 9 because their
# square roots would all equal 2 in integer form. I called my function in an if statement so I could print the results cleanly. This probably
# isn't the easiest method, but I found this way fun.



import math         #Importing the math module

N = input("Enter a number to check if it is a prime: ")         #Asking kindly for an input

num = N.isnumeric()     #This is a function I found in the Python docs to verify a number. Link: https://docs.python.org/3/library/stdtypes.html?highlight=isnumeric#str.isnum

while num == False:     #A while loop to test if the input is a numeber
    N = input("Stop trying to break my code and enter a positive integer: ")          #Asking not so kindly to input a number
    num = N.isnumeric()         #Testing the new input to see if its a number

IntN = int(N)       #Once the input has been verified a number, I turn it into a integer

SqrtN = int(math.sqrt(IntN))        #Finding the square root of the input

def pTest(input):               #Creating a function to test for prime
    if input < 2:               #If the input is less than 2 it instantly knows its not prime.
        return False
    for x in range(2, SqrtN + 1):         #This for loop tests all integers form 2 through the square root of the input plus one
        if input % x == 0:              #This tests every integer if it evenly divides the input
            return False            #Returns false if the input can be divided
    return True             #Else returns true for it being prime
        
if pTest(IntN) == True:         #Calls the prime test, and then prints the corresponding statment to the console.
    print("Your number is prime!")
else:
    print("Your number is NOT prime!")
