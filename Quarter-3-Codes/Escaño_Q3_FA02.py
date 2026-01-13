#Planning a Mini-Dataset Project
steps = [
    ["Me",   4500, 5200, 4800, 5000, 5300],
    ["Lia",  4000, 4100, 3900, 4200, 4600],
    ["Jake", 6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

jake_row = 2
wednesday_col = days.index("Wednesday") + 1
print("Jake's steps on Wednesday: ", (steps[jake_row][wednesday_col]))

me_row = 0
my_steps = []
for i in range(1, len(steps[me_row])):
    my_steps.append(steps[me_row][i])

print("My steps... " , my_steps)

print("Average steps of each person:")
total_steps = 0
total_days = 0

for i in steps:
    name = i[0]
    daily_steps = []
    for x in range(1, len(i)):
        daily_steps.append(i[x])
    avg = sum(daily_steps) / len(daily_steps)
    print(name , "'s average steps:", avg)
    total_steps += sum(daily_steps)
    total_days += len(daily_steps)

overall_avg = total_steps / total_days
print("Average steps of everyone: ", overall_avg)

#Kaelyn Anne D Escaño - 8 Rosal