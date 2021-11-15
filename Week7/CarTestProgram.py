from CarClass import car

AudiTT = car("black", 2.0, 2, 2)
HondaAccord = car("white", 1.8, 4, 4)
ToyotaRav4 = car("red", 2.6, 4, 4)
ChevyMalibu = car("grey", 2.0, 4, 4)

print(AudiTT.color, HondaAccord.color, ToyotaRav4.color, ChevyMalibu.color)

HondaAccord.repaintCar()
AudiTT.tintWindows()

print(AudiTT.tint)
print(HondaAccord.color)

