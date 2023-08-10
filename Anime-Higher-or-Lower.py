import csv
import random
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Getting date from file
def get_data():
    file = open("myAnimeListDataset.csv", encoding="utf8")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows

rows = get_data()
wrong = False
score = 0
first = rows[random.randint(0,len(rows))]
count = 0

while not wrong:
    os.system('cls')
    print(logo)
    if count >= 2:
        first = rows[random.randint(0,len(rows))]
        count = 0
    second = rows[random.randint(0,len(rows))]

    if second == first:
        second = rows[random.randint(0,len(rows))]

    if first[2] > second[2]:
        max = "A"
    else:
        max = "B"

    print(f"A: {first[1]}")
    print(vs)
    print(f"B: {second[1]}")

    answer = input("Choose A or B: ")
    if answer == max:
        score += 1
        print("Correct answer!")
        print(f"Your score now is {score}")
        input("Press Enter to start the next round")
        if max == "B":
            first = second
        count += 1
    else:
        wrong = True
        
print(f"You lost and your final score is {score}")