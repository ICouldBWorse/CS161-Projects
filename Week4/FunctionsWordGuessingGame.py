#Dustin Erickson
#CS 161
#10-25-21
#See the design file attached with this one for an overview of my program.




import random       #I will be using random.randint and random.choice

#Initializing my variables, my list of words, and setting my random phrase and random amount of money.
gameInit = False
phrases = ["hello", "orange", "table", "water","computer","science","math","purple","golf","river", "mountain","death", "goat",
"world", "tomato", "door", "power", "climb", "green","oscillate"]
phrase = (random.choice(phrases))
spin = ("")
playerMoney = 1000
money = random.randrange(300,800,100)
word = list(phrase)
guess_word = ['*' for x in word]

#Printing the rules and creating the function rules.
def rules():
    print('Welcome to Wheel of Misfortune! You will try to guess the letters in a word.') 
    print('Before the round you will be asked to "spin" for the amount that each guess is worth.')
    print('You will recieve the amount you spin for each correct letter. We are giving you $1000 to start.')
    print('When you guess an incorrect letter, you will loose $500. If you drop below $0, you loose the game.')
    print('If you guess the whole word, you win the total amount of money!')
    global start
    start = input("Are you ready to play? y/n           ")




#This prompts the user to input the letter y to start the game. If y is not seen it will continue to ask. Once y is given it asks the user 
#to type spin to "spin" for the amount of money. (It has already been assigned in the variable, but making them type it adds to the experiencey)
#It also initializes the function startGame. 
def startGame(Init, start, spin):
    while Init == False:
        if start == ("y"):
            if spin ==("spin"):
                print("You spun " + str(money) + " dollars!")
                Init = True
                break
            else:
                spin = input("Please type 'spin' to spin the Wheel of Misfortune!    ")
        else:
            print("Please type 'y' when ready to continue.")
            start = input("Are you ready to play? y/n           ")


#I tried for hours to implement a system from scratch to replace the characters in a list with stars, and then swap the letters when they were
#guessed correctly. I shamelessly borrowed this idea from https://python-forum.io/thread-11130.html. I just needed the function to swap the 
#symbols from * to letters. The original code is benath my project. (I hope this is a good enough citation, if you need more please let me know)

def check(char, word, guess_word):
   

    for c in word:
        if c == char:
            guess_word[word.index(c)] = c
            word[word.index(c)] = '*'
 
    return guess_word




#Main while loop. It says that while their is a * in the word, it will continue. I added a few if statements to manage the money system and
#print the money.
def gameLoop(Money):
    while '*' in guess_word:
        if Money < 0:
            break
    
        guess = input('Guess: ')
        if guess not in word:
            Money = Money - 500
            print("Incorrect\nYou now have " + str(Money) + " dollars.")
        elif guess in word:
            Money = Money + money
            print("Correct!\nYou now have " + str(Money) + " dollars.")
        print(check(guess, word, guess_word))
    return Money


#If you have more than 0 dollars, it prints you win. If you have 0 or less it prints you went bankrupt. This also creates the function endGame.
def endGame(money):
    if money > 0:
        print("\n\n\nYou win " + str(money) + " dollars!\n\n\n")
    else:
        print("You went BANKRUPT!")

#This creates the function Main(). It contains the other functions defined previously.
def main(money, phrases, guess_word):
    
    rules()
    startGame(gameInit,start,spin)

    print(guess_word)

    playerMoney = gameLoop(money)
    endGame(playerMoney)


#calls the main function with the variables needed.
main(playerMoney, phrases, guess_word)


#             APPENDIX:
#
# def checkLetter(letter, word, guess_word):
# 
#   for c in word:
#      if c == letter:
#            guess_word[word.index(c)] = c
#            word[word.index(c)] = '*'
# 
#    return guess_word
# 
# word = list('apple')
# guess_word = ['_' for x in word]
# 
# print(guess_word)
# while '_' in guess_word:
#    guess = input('Letter: ')
#    print(checkLetter(guess, word, guess_word))
