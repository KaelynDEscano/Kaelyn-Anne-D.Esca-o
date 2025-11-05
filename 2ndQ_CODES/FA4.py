import random

#I improvised this code from the flowchart I passed in the filler because it was very plain. 😭

print("⭐ If it displayed any Value Error, please re-run the code again, ma'am! ⭐")

#Main inputs from user + Main variables! 💛💛💛💛💛💛💛

# I had to ask help again from my brother because it started to not accept other inputs other than integers. 😭
while True:
    try:
        studentno = int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Bruh I say enter whole integer only.")

while True:
    try:
        subjectno = int(input("Enter the number of subjects: "))
        break
    except ValueError:
        print("Bruh I say enter whole integer again!!!")

CLASS = 0

EMOJIS = ("💔" , "😂" , "🤤" , "❤️" , "🌻" , "🌻" , "💢" , "💦" , "🎈" , "🍟" , "🥩" , "🍚" , "😎" , "🖊️" , "🔍")

RANDOM = random.choice(EMOJIS)

#For Loop 😢

for student in range(1, studentno + 1):
    print("Student", student , RANDOM)
    total = 0

    for subject in range(1, subjectno + 1):

        #I had to ask help again because it started to not accept other inputs other than integers.😭
        while True:
            try:
                score = int(input(f"Enter score for Subject {subject}: "))
                break 
            except ValueError:
                print("Please try again but use a whole number.")
        total = total + score

    average = total / subjectno
    raverage = round(average, 2)

    print("Average of Student" , student , RANDOM , "is " , raverage)

    CLASS = CLASS + raverage

avg = CLASS / studentno
ravg = round(avg, 2)

#RESULTS ✨

if avg == 100:
    print("Class Average is", ravg, ", This class is perfect! 🏅")

elif avg >= 90:
    print("Class Average is", ravg, ", This class is excellent! 🌟")

elif avg >= 80:
    print("Class Average is", ravg, ", This class is good! 😃")

elif avg >= 70:
    print("Class Average is", ravg, ", This class is average! 👍")

elif avg >= 60:
    print("Class Average is", ravg, ", This class is poor! 💔")

else:
    print("Class Average is", ravg, ", This class failed... 😢")

#Kaelyn Escaño - Rosal