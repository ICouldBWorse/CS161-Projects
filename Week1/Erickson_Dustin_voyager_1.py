# Dustin Erickson
# 10/04/2021
# Homework Problem 3
# I made the calculations, converted them into the nessecary units, and then printed them to the console. The variables and calculations are
# above, the print statments are below.


veloMPH = 38241       #velocity of Voyager in MPH
Distance0 = 16637000000        #Distance at day 0
Date = int(input("How many days has it been since 9/25/09? "))  #I prompted the user for the number of days passed since day 0
HoursPassed = Date * 24         #I converted the numbers of days passesed to hours
DistanceMiles = Distance0 + (veloMPH * HoursPassed)      #Added the start distance to the number of hour times the miles per hour
DistanceKilometers = int(DistanceMiles * 1.609344)   #I converted the distance in miles to kilometers
DistanceAU = DistanceMiles / 92955887.6          #I converted the distance in miles to Astronomical Units
LightHr = 299792458 * 60 * 60            #Speed of light in meters per hour
RoundTripMeters = (DistanceKilometers * 2) * 1000        #I multiplied the kilometers by 2 to get round trip, then multiplied by 1000 to get meters
RoundTripHrs = RoundTripMeters / LightHr        #I divided the total roundtrip distance in meters by the speed of light in meters per hour


#Printing each calculation and converting the integers into strings.
print("Voyager is " + str(DistanceMiles) + " miles from the sun.")
print("Voyager is " + str(DistanceKilometers) + " kilometers from the sun.")
print("Voyager is " + str(DistanceAU) + " astronomical units from the sun.")
print("It will take " + str(RoundTripHrs) + " hours for a radio signal to reach voyager and come back to the sun.")
