buget = 6000

print ("Welcome to the family vacation buget calculator! \nYou have a buget of $6000 dollars to spend on your vacation!")
fam = int(input("Ammount of family members: "))
airfair = float(input("Money spent on air travel per person: "))
food = float(input("Money spent on food per person: "))
days = int(input("Number of days for this trip: "))
excurtion = float(input("Money spent on activities: "))
souv = float(input("Money spent on souveniers: "))

total = (airfair * fam) + (food * fam * days) + excurtion + souv
if total <= buget:
    buget -= total
    print ("\nYou're under buget!")
    print (f"The remainder is ${buget:.2f}.")
    print (f"\nYou spent: ")
    airfair = airfair * fam
    print (f"${airfair:.2f} on airfair,")
    food = food * fam * days
    print (f"${food:.2f} on food,")
    print (f"${excurtion:.2f} on activities,")
    print (f"and ${souv:.2f} on souveniers.")

elif total > buget:
    buget -= total * -1 - 6000
    print (f"\nYou're over buget by ${buget:.2f}.")
    print (f"\nYou spent: ")
    airfair = airfair * fam
    print (f"${airfair:.2f} on airfair,")
    food = food * fam * days
    print (f"${food:.2f} on food,")
    print (f"${excurtion:.2f} on activities,")
    print (f"and ${souv:.2f} on souveniers.")
