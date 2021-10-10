# Dustin Erickson
# 10-9-2021
# This is a very short program that prints the word pbil if the word alphebetical is typed by the user. I chose to print pbil 12 times, once per
# letter in the word alphebetical. If the word is not typed, then it prints something else. 


phrase = input("Please enter the secret phrase: ")      #asks user for an input phrasae

if phrase == "alphebetical":            #tests if the phrase in the word alphebetical
    for x in range(0, 12):          #runs this loop 12 times
        print("pbil")           # prints the word pbil
else:
    print("Not pbil :(")        #prints not pbil :(