#Input
radius = float(input("Enter the radius of the circle: "))

#Values
pi = 3.14159

#Radius to Area of circle

radius2 = radius * radius or radius ** 2

#Area of circle formula:
Area = pi * radius2

#Rounding to 2 decimal places
Area2 = round(Area, 2)

print("The area of the circle is:", Area2 ,"square units.")
