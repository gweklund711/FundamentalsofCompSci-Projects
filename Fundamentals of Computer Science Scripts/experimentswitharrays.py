# For one of my assignments, I had to create a script that performs a variety of functions on an array of numbers.
# The first function that it performs is taking in a number and telling the user whether it is an even or odd number.
# From there, the program prints the first value in the array, the last value in the array, and the third number in the
# array.Then, it adds in 25 to the end of the array and prints the modified array
# Finally, it tests whether the array is empty, clears the entire array, and then it tests again.
coolNumbers = [7, 4, 38, 21, 16, 15, 12, 33, 31, 49]
for n in coolNumbers:
    if n%2==0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")
print(f"The first number in the array is {coolNumbers[0]}.")
print(f"The last number in the array is {coolNumbers[-1]}.")
print(f"The third number in the array is {coolNumbers[2]}.")
coolNumbers.append(25)
print(f"The array with 25 added in at the end is {coolNumbers}.")
if len(coolNumbers) == 0:
	print("The array is empty.")
else:
	print("The array is not empty")
coolNumbers.clear()
print(f"The array with all values removed is {coolNumbers}.")
if len(coolNumbers) == 0:
	print("The array is empty.")
else:
	print("The array is not empty")
