# This script reads in inputted grades of 3 tests, and determines the average.
# From there, the project determines the letter grade (based on Texas' passing score of 70)
# that the user would receive.
print("Welcome to the Letter Grade Calculator.")
print("This program will tell you your letter grade based on a grade average.")
print("First, you will need to input some test scores for the program to determine the average.")
print("")

# This section below can be modified to include more or less test scores
print("Please type in the first test score here: ")
scoreOne = int(input())
print("Please type in the second test score here: ")
scoreTwo = int(input())
print("Please type in the third test score here: ")
scoreThree = int(input())

print("")
averageGrade = float(round(((scoreOne + scoreTwo + scoreThree) / 3), 1))
print(f"Based on these test scores, your grade average is a {averageGrade}.")
print("Now, the calculator will determine your letter grade based on this average.")
print("")
letterGrade = "X"

if 0 <= averageGrade <= 69:
    letterGrade = "F"
elif 70 <= averageGrade <= 71:
    letterGrade = "D"
elif 72 <= averageGrade <= 74:
    letterGrade = "C-"
elif 75 <= averageGrade <= 76:
    letterGrade = "C"
elif 75 <= averageGrade <= 76:
    letterGrade = "C"
elif 77 <= averageGrade <= 79:
    letterGrade = "C+"
elif 80 <= averageGrade <= 83:
    letterGrade = "B-"
elif 84 <= averageGrade <= 86:
    letterGrade = "B"
elif 87 <= averageGrade <= 89:
    letterGrade = "B+"
elif 90 <= averageGrade <= 93:
    letterGrade = "A-"
elif 94 <= averageGrade <= 96:
    letterGrade = "A"
elif 97 <= averageGrade <= 100:
    letterGrade = "A+"
else:
    letterGrade = "ERROR OCCURRED"

print(f"With an average score of {averageGrade}, your letter grade would be a(n) {letterGrade}.")