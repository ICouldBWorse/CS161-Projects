import random

##Part 1

#Original
ListofNumbers = [10,20,76,89,111]
print("Original List:", ListofNumbers)

#Add & Insert - Adds a number at the end of the list, inserts a number at a given index in the list
ListofNumbers.append(137)
print("List with item added:", ListofNumbers)
ListofNumbers.insert(2,23)
print("List with item inserted:", ListofNumbers)

#Modify - Changes data at a given index
ListofNumbers[3] = 99
print("Modified List:", ListofNumbers)

#Remove & Pop - Remove deletes what ever is given as the paramater from the list, pop deletes whatever is at the index of the paramater.
ListofNumbers.remove(20)
print("List with item removed:", ListofNumbers)
ListofNumbers.pop(0)
print("List with number popped:", ListofNumbers)

#Index - Takes a number as a parameter and determines its index
Index = ListofNumbers.index(111)
print("The index of the value 111 is", Index)

#Function to determine list mean
def listMean(numList):
    S = 0
    for x in range(len(numList)):
        S = numList[x] + S
    Avg = S / len(numList)
    return Avg
    
    
#Calling the list mean function
print(listMean(ListofNumbers))

#Function to find information about your fingers
#Fake Finger lengths 2.3 3.1 4.6 4.1 3.2 3.4 4.0 4.8 4.6 3.0

#FingerLengths = input("Please input the length of your fingers in order from left pinky to right pinky seperated by space: ")
FingerLengths = [2.3, 3.1, 4.6, 4.1, 3.2, 3.4, 4.0, 4.8, 4.6, 3.0]
#fingerList = FingerLengths.split()
fingerList = FingerLengths
fingerNames = ["Left Pinky", "Left Ring", "Left Middle", "Left Pointer", "Left Thumb", "Right Thumb", "Right Pointer", "Right Middle", "Right Ring", "Right Pinky"]

for x in range(len(fingerList)):
    fingerList[x] = float(fingerList[x])

LongFingIndex = fingerList.index(max(fingerList))
LongFingName = fingerNames[LongFingIndex]

ShortFingIndex = fingerList.index(min(fingerList))
ShortFingName = fingerNames[ShortFingIndex]

AvgFingerLength = listMean(fingerList)

fingerSum = sum(fingerList)

print("You're longest finger is your", LongFingName)
print("You're shortest finger is your", ShortFingName)
print("Average length of you're fingers is", AvgFingerLength, "inches.")
print("You're fingers total a length of", fingerSum, "inches.")





#Part 2

#Creating a tuple
tupleOfNum = (12,3,4,9)
print("The original Tuple is:", tupleOfNum)

#You can't add to a touple
#You can't change data in a touple
#You can't remove data in a touple

#Finding the index value of a given number in the tuple
tupleIndex = tupleOfNum.index(4)
print("The index of the number 4 in the tuple is", tupleIndex)



#Function created to find the mean of a tuple
def tupleMean(numTup):
    S = 0
    for x in range(len(numTup)):
        S = numTup[x] + S
    Avg = S / len(numTup)
    return Avg

print("The mean of the tuple is", tupleMean(tupleOfNum))

#Function to find information about your fingers
#Fake Finger lengths 2.3 3.1 4.6 4.1 3.2 3.4 4.0 4.8 4.6 3.0

#TupFingerLengths = input("Please input the length of your fingers in order from left pinky to right pinky seperated by space: ")
TupFingerLengths = ("2.3 3.1 4.6 4.1 3.2 3.4 4.0 4.8 4.6 3.0")
fingerPreTuple = TupFingerLengths.split()

for x in range(len(fingerPreTuple)):
    fingerPreTuple[x] = float(fingerPreTuple[x])

fingerTuple = tuple(fingerPreTuple)

TupfingerNames = ("Left Pinky", "Left Ring", "Left Middle", "Left Pointer", "Left Thumb", "Right Thumb", "Right Pointer", "Right Middle", "Right Ring", "Right Pinky")


TupLongFingIndex = fingerTuple.index(max(fingerTuple))
TupLongFingName = TupfingerNames[TupLongFingIndex]

TupShortFingIndex = fingerTuple.index(min(fingerTuple))
TupShortFingName = TupfingerNames[TupShortFingIndex]

AvgFingerLengthTup = tupleMean(fingerTuple)

fingerSumTup = sum(fingerTuple)

print("You're longest finger is your", TupLongFingName)
print("You're shortest finger is your", TupShortFingName)
print("Average length of you're fingers is", AvgFingerLengthTup, "inches.")
print("You're fingers total a length of", fingerSumTup, "inches.")



#Part 3

##I am creating a lottery calculator that uses a list of people then determines how much they win using a tuple for prize money.

names = ["Fred", "Steve", "Bob", "Kylee", "Beth", "Sherri"]
prizes = (500,250,100,50,25,0)

def lotoWinner(people, money):
    print("These are the current participants:", people)
    print("The current prizes are:", money)
    winner = random.choice(people)
    amount = random.choice(money)
    if amount == 0:
        print("Sorry, nobody wins.")
    else:
        print(winner, "wins", amount, "dollars!")

lotoWinner(names, prizes)

listOfFood = ["Burgers", "Pizza", "Ice Cream", "Burrito", "Raviolli"]

favFood = input("Please guess my favorite food: ")

if listOfFood.count(favFood)>0:
    print("That's my favorite food!")
else:
    print("That is not my favorite food.")