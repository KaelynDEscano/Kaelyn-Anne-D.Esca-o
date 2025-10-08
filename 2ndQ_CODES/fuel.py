def calculate(distance_traveled, fuel_consumed):
    if distance_traveled < 0 or fuel_consumed <= 0:
        raise ValueError("Distance traveled must be non-negative and fuel consumed must be positive")
    return distance_traveled / fuel_consumed

#Input from user!
DT = float(input("Enter the distance traveled (in kilometers): "))
FC = float(input("Enter the fuel consumed (in liters): "))
FUEL_EFF = calculate(DT, FC)

#Output...
print("Fuel Efficiency", round(FUEL_EFF, 2), "km/L")

#WOW Kaelyn Escaño - Rosal