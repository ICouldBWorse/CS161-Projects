# Dustin Erickson
# 10-9-2021
# This program calculates the number of grains of wheat if it doubles based on the number of squares of a chess board. I used a for loop to 
# act as a summation of 2^x from 0 to 64(64 total iterations because the upperbound is not inclusive). I then just converted the number of 
# grains into their mass. I also found surface area and height with the assumption that each grain is 10mm long, 1mm wide, and 1mm tall.


sum = 0     #sum of grains
for x in range(0,64):       #For function that counts the grains. It acts as a summation
    sum = (2 ** x) + sum      

#Grain weight: 50 mg

massMg = sum * 50           #Calculates the weight of mass in mg, then the next line converts it into kgs.
massKg = massMg/1000000

#grains diamensions: 10mmW * 1mmL * 1mmH

SurfaceAreaMm = sum * 10 * 8        #Calculates surface area in mm
SurfaceAreaKm = SurfaceAreaMm / 10000000000         #converts surface area from mm to km
Height = (SurfaceAreaKm / 254806) / 1000000         #Calculates the height of the entire area in km.


#Prints my answers

print("Grains of wheat: ", sum)        
print("Mass of the grains in Kg: ", massKg)
print("Height of the grains covering the state of Oregon in Km: ", Height)
