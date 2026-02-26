steps = [
    ["Me",   4500, 5200, 4800, 5000, 5300],
    ["Lia",  4000, 4100, 3900, 4200, 4600],
    ["Jake", 6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(len(steps)):
    name = steps[i][0]
    total_steps = sum(steps[i][1:])
    average_steps = total_steps / (len(steps[i]) - 1)
    print(name + " walked a total of " , total_steps , " steps and an average of " , average_steps , " steps per day.")

max_steps = 0
min_steps = float('inf')
for i in range(len(steps)):
    for j in range(1, len(steps[i])):
        if steps[i][j] > max_steps:
            max_steps = steps[i][j]
        if steps[i][j] < min_steps:
            min_steps = steps[i][j]
print("The maximum steps taken in a day is: " , max_steps)
print("The minimum steps taken in a day is: "  , min_steps)

#Kaelyn Anne D. Escaño - 8 Rosal