# Aliyah Simpson
# 10/29/2026
# Teaching input validation and using loops

# Ask for number of scores user wants to enter
score_num = int(input("How many scores do you want to enter? "))

# create an empty list
scores = []

for num in range(1, score_num +1):
    
    # collect scores
    score = float(input(f"Enter score #{num}: "))
    
    # evaluate entry
    while score > 100 or score < 0:
        print("INVALID score entered!")
        print("Score should be between 0 and 100!")
        
        score = float(input(f"Enter score #{num}: "))
# Add validated score to the list
    scores.append(score)
    print(scores)
    
lowest_score = min(scores)

print(f"Lowest grade: {lowest_score}")

# Remove lowest grade from list
scores.remove(lowest_score)

print(scores)