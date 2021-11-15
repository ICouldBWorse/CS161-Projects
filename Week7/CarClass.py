class car:
    def __init__(self, color, engineSize, doors, seats):
        self.color = color
        self.engineSize = engineSize
        self.doors = doors
        self.seats = seats
        self.tint = 0
        self.muffler = "stock"

    def repaintCar(self):
        print("The car's current color is: ", self.color)
        self.color = input("Please enter the color you would like to paint your car: ")
        print("The new car color is: ", self.color)

    def tintWindows(self):
        self.tint = int(input("Please enter the percent sunlight rating of the desired tint for your windows: "))
        print("The new car tint is: ", self.tint)

    def replaceMuffler(self):
        self.muffler = input("Please enter the name of the new muffler you would like to add: ")
        print("The new car muffler is: " + str(self.muffler))
    


