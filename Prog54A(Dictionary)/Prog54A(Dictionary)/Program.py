﻿car = {
    "1970 VW Buv": (286, 9),
    "1979 Firebird": (412, 40),
    "1980 Subaru": (361, 18), 
    "1975 Cutlass": (161, 11)
}

print("Choose a car from the following:", cars.keys())
mycar = input()
miles, gallons = cars[mycar]
mpg = float(miles) / gallons
print("Miles: ", miles)
print("Gallons: ", gallons)
print("MPG: ", round(mpg, 1))

input()