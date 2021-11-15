from CarClass import car


def carMenu():
    idealCar = car(input("What color would you like your car to be? "),float(input("How big of a car engine do you want? ")), 
    int(input("How many doors do you want on your car? ")), int(input("How many seats do you want your car to have? ")))

    confirm = input("Please confirm: " + str(idealCar.color) + " " + str(idealCar.engineSize) + " liters " + str(idealCar.doors) + " doors and "+ str(idealCar.seats) + " seats. (y/n) ")

    if confirm == "n":
        carMenu()
    
    print("We offer additional services! Would you like to repaint your car, tint your windows, or add a new muffler?")
    done = False

    while done == False:
        service = input("Please enter 'tint', 'muffler', 'color', 'current', or 'none' to select a service: ")
        if service == "tint":
            idealCar.tintWindows()
        elif service == "muffler":
            idealCar.replaceMuffler()
        elif service == "color":
            idealCar.repaintCar()
        elif service == "none":
            print("We hope you like your new car!")
            done = True
        elif service == "current":
            print(str(idealCar.color) + "    " + str(idealCar.engineSize) + " liters    " + str(idealCar.doors) 
            + " doors and "+ str(idealCar.seats) + " seats    " + str(idealCar.muffler) + " muffler   " + str(idealCar.tint) + " percent sunlight")
        else:
            print("Please enter a recognized command.")



carMenu()
