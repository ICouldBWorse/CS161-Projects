#Part 1

#Creating a dictionary called gradebook
gradebook = {"Project 0" : 100, "Project 1" : 99, "Project 2" : 94, "Project 3" : 87}
print(gradebook)

#Adding data to a dictionary and printing it
gradebook["Project 4"] = 96
print(gradebook)

#Changing data attached to a key and then printing the new dictionary
gradebook["Project 3"] = 91
print(gradebook)

#Using "pop" to remove an entry from the dictionary and then printing it
gradebook.pop("Project 0")
print(gradebook)

#Indexing a dictionary and printing it
print(gradebook["Project 3"])

#creating a mean function to find the average of this dictionary and then printing it
def meanDict(workingDict):
    s=0
    for a in workingDict.values():
        s = a + s
    s = s / len(workingDict)
    return s

print("Your grade is:", meanDict(gradebook))

#This is a function that clears all previous items in the gradebook, and then it asks the user to input the number of assignments they have,
#the name of the assignment, and the score on the assignment.

gradebook = {}
gradebookDone = False
print("Please enter the score of each assignment, and then the name attached to each score.")
while gradebookDone == False:
    gradebook[input("Please input the name of the assignment: ")] = int(input("Enter your score: "))
    done  = input("Would you like to add another assignment (y/n): ")
    if done == "n":
        gradebookDone = True
    else:
        gradebookDone = False


def maxDict(workingDict):
    x = -99999999999999999999999999999
    for a in workingDict.values():
        if a > x:
            x = a
    return x

def minDict(workingDict):
    x = 100000000000000000000000000000
    for a in workingDict.values():
        if a < x:
            x = a
    return x


print(gradebook)
print("Your average grade is: ", meanDict(gradebook))
print("Your highest grade is: ", maxDict(gradebook))
print("Your lowest grade is: ", minDict(gradebook))



