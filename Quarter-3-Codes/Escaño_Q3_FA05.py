names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

day_totals = []
for col in range(len(days)):
    total = 0
    for row in range(len(names)):
        total += steps[row][col]
    day_totals.append(total)
    print("Total steps on " , days[col], ": ", total)

max_total = max(day_totals)
max_index = day_totals.index(max_total)
print("Most active day: " , days[max_index] , " (" , max_total , " steps )")

#Kaelyn Anne D Escaño - 8 Rosal
