#Returns the total delivery fee per kilometer!
def calculate(delivery_distance, delivery_rate):

    if delivery_distance < 0 or delivery_rate < 0:
        raise ValueError("Distance and rate must be non-negative")
    return delivery_distance * delivery_rate

#Input from user!
DD = float(input("Enter the delivery distance in kilometers: "))
DR = float(input("Enter the delivery rate per kilometer (₱): "))
DISFEE= calculate(DD, DR)

#Output...
print("The delivery total fee is: ₱", DISFEE)

#Kaelyn Escaño - Rosal