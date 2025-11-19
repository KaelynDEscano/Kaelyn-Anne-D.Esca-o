Destination = []

print("Enter 5 destinations ✈️:")
for num in range(5):
    num = num + 1
    place = input("Destination " + str(num) + ": ")
    Destination.append(place)

print("Your destinations are:")
for num in range(5):
    num = num + 1
    print("Destination " + str(num) + ": " + Destination[num - 1])

print("Update your 2nd and 5th destinations for whatever reasons! ✍️:")
two = input("Enter a new destination for position 2: ")
five = input("Enter a new destination for position 5: ")

Destination.pop(1)
Destination.pop(4 - 1)

Destination.insert(1, two)
Destination.insert(4, five)

print("Your new destinations are:")
for num in range(5):
    print ("Destination " + str(num + 1) + ": " , Destination[num])

for row in range(1):       
    for col in range(24):     
        print(" - ✈️ -", end=" ")
    print()
#Kaelyn Escaño - Rosal