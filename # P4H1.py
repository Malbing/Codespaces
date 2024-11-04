# P4H1
# 11/4/2024
# Grabbing grades from the user, using a loopfor the user to input grades, then averaging the scores

# Grabbing the amount of scores from the user
scores = int(input("How many scores do you want to enter? "))

# Empty list
scorelist = []

for items in range(0, scores):
    userInput = float(input(f"Enter score #{items+1} "))
    while userInput <0 or userInput >100:
        print("INVALID Score Entered!!!!")
        print("Score should be between 0 and 100")
        userInput = float(input(f"Enter score #{items+1} "))
    scorelist.append(userInput)

print()
print()
print(f"---" * 10, "Results", "---" *10)
print(f"Lowest Score: {min(scorelist)}")
print(f"Modified List: {scorelist}")
print(f"Scores Average: {sum(scorelist)}")
         