
from math import floor

eggs = int(input("Enter number of eggs: "))
dozens = floor(eggs / 12)
remaining = eggs % 12
prc = 0.0
ttl = 0.0
if dozens > 0 and dozens <= 4:
    price = 0.50
elif dozens > 4 and dozens <= 6:
    price = 0.45
elif dozens > 6 and dozens <= 11:
    price = 0.40
elif dozens > 11:
    price = 0.35
else:
    print("Invalid amount of eggs")
ttl = (dozens * price) + remaining * (price / 12)
print("Price per: $" + str(price))
print("Total Cost: $%.2f" % float(ttl)) 
input()