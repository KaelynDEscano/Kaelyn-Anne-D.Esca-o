#Returns the cost
def calculate(kilowatt_hours):
    if kilowatt_hours < 0:
        raise ValueError("Kilowatt hours must be non-negative")
    elif kilowatt_hours <= 100:
        return kilowatt_hours * 5.00
    elif (kilowatt_hours <= 300):
        return (100 * 5.00) + ((kilowatt_hours - 100) * 7.00)
    elif kilowatt_hours <= 500:
        return (100 * 5.00) + (100 * 7.00) + ((kilowatt_hours - 200) * 10.00)
    elif kilowatt_hours > 500:
        return (100 * 5.00) + (100 * 7.00) + (300 * 10.00) + ((kilowatt_hours - 500) * 12.00)
    
    #Input from user!
KH = float(input("Enter the number of kilo-watt hours used: "))
COST = calculate(KH) + 50

#Output...
print("The total cost of electricity is: ₱", round(COST, 2))