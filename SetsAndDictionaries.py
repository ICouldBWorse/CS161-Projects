#Part 3
from functools import reduce
from operator import or_

recipies = {"Pizza" : {"Dough", "Sauce", "Cheese"}, 
            "Cheeseburger" : {"Buns", "Burger", "Cheese", "Toppings"}, 
            "Pasta" : {"Sauce", "Noodles","Cheese"},
            "Fried Chicken Sandwich" : {"Breading", "Chicken", "Buns", "Toppings"}}

pantry = {"Sauce", "Cheese", "Chicken", "Buns", "Burger", "Toppings"}


def dinner(dict,set):
    if set.intersection(dict["Pizza"]) == dict["Pizza"]:
        print("You can make a Pizza")
    elif set.intersection(dict["Cheeseburger"]) == dict["Cheeseburger"]:
        print("You can make a Cheeseburger")
    elif set.intersection(dict["Pasta"]) == dict["Pasta"]:
        print("You can make Pasta")
    elif set.intersection(dict["Fried Chicken Sandwich"]) == dict["Fried Chicken Sandwich"]:
        print("You can make a Fried Chicken Sandwich")


dinner(recipies,pantry)


Keys = ["Dustin", "Kevin", "Sara"]
Values = [18, 16, 15]


NewDict = dict(zip(Keys, Values))
  

print ("The new dictionary is: " +  str(NewDict))