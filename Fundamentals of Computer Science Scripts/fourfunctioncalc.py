# Basic calculator that performs one of four defined functions on two inputted numbers. The user can select an option, and a function will 
# be performed based on that selection.
print("Welcome to the basic four function calculator!")
print("Please input the first number here:")
numOne = float(input())
print("Please input the second number here:")
numTwo = float(input())

def addNums():
	numSum =  round((numOne + numTwo), 1)
	return numSum
def subNums():
	numDif = round((numOne - numTwo), 1)
	return numDif
def mulNums():
	numPro = round((numOne * numTwo), 1)
	return numPro
def divNums():
	numQuo = round((numOne / numTwo), 1)
	return numQuo

print(f"You have inputted {numOne} and {numTwo} into the calculator.")
print("Now, you can select one of these four functions to perform on the values.")
print("1. Additon")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
menuOption = int(input())

if menuOption == 1:
	print(f"The sum is about {addNums()}.")
elif menuOption == 2:
	print(f"The difference is about {subNums()}.")
elif menuOption == 3:
	print(f"The product is about {mulNums()}.")
elif menuOption == 4:
	print(f"The quotient is about {divNums()}.")
else:
    print("ERROR OCCURRED")