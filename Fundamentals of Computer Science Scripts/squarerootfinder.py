# With this script, a user can enter any whole number between 1-10,000. Once they input the number, the program will
# search for a perfect square root.
print("Type in a whole number between 1-10,000 here:")
num = int(input())
sqrt = int(0)
if num > 10000 or num < 1:
	print("Restart and pick a whole number within the range.")
for i in range(1, 100):
	if num == i * i:
		sqrt = i
if 0 == sqrt:
	print("No Perfect Square Root")
else:
	print(f"The square root of {num} is equal to {sqrt}")
