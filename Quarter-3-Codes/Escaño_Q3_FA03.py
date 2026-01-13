names = ["Me", "Lia", "Jake"]

steps = [
    ["Me",   4500, 5200, 4800, 5000, 5300],
    ["Lia",  4000, 4100, 3900, 4200, 4600],
    ["Jake", 6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print("----- Daily steps -----")
for x in steps:
    print(x[0], ": " , x[1:])

overall_max = steps[0][1]
overall_min = steps[0][1]

for x in steps:
    name = x[0]
    
    Daily_steps = []
    for i in range(1, len(x)):
        Daily_steps.append(x[i])

    total = sum(Daily_steps)
    avg = total / len(Daily_steps)
    
    person_max = max(Daily_steps)
    person_min = min(Daily_steps)

    print(name, "- Total:", total, " Average:", avg, " Max:", person_max, " Min:", person_min)

#I used chat gpt to help me with the slicing of array part since I am not yet familiar with it. Found at line 13 with x[1:]