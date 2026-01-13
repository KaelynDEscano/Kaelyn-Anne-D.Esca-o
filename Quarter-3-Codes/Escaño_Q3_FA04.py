names = ["My", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []
for i in range(len(names)):
    total = sum(steps[i])
    totals.append(total)
    print((names)[i], "total steps:", total)

max_total = max(totals)
min_total = min(totals)
max_index = totals.index(max_total)
min_index = totals.index(min_total)
print("Person with the highest total steps: ", (names[max_index]), " with ", max_total, "steps")

dif = max_total - min_total
print("Difference between highest " , "(" , (names[max_index]) , ")" , " and lowest " , "(" , (names[min_index]) , ")" , " total steps: " , dif)

#Kaelyn Anne D Escaño - 8 Rosal