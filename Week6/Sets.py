#Part 2

#Creating a set(and empty set) and printing them
emptySet = set()
print(emptySet)

eceSet = {"Calculus", "Physics", "Chemistry", "Electrical Fundementals", "Computer Science", "Digital Logic", "Discrete Math"}
print(eceSet)

#Adding data to a set and printing it
eceSet.add("Biology")
print(eceSet)

#Can not change data in a set becasue their are no keys or indexes in sets

#Removing a specific item in a set, and clearing the entire set.
eceSet.remove("Computer Science")
print(eceSet)

eceSet.clear()
print(eceSet)


#There are no indexes in sets


#Function that finds the intersection of two sets

def intersect(setA, setB):
    intersectSet = set()
    for a in setA:
        if a in setB:
            intersectSet.add(a)
    return intersectSet



eceSet = {"Calculus", "Physics", "Chemistry", "Electrical Fundementals", "Computer Science", "Digital Logic", "Discrete Math"}
CompSciSet = {"Calculus", "Computer Science", "Discrete Math", "Data Structures"}

print(intersect(eceSet, CompSciSet))


#Functions to find the Intersect, Union, and difference of two sets.

intersectSet = eceSet.intersection(CompSciSet)
unionSet = eceSet.union(CompSciSet)
eceDifference = eceSet - CompSciSet
csDifference = CompSciSet - eceSet

print(intersectSet)
print(unionSet)
print(eceDifference)
print(csDifference)
