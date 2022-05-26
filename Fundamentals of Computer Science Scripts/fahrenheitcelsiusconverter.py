# This program has the purpose of either converting from Celsius to Fahrenheit or from Fahrenheit to Celsius. 
# The user is able to select which converter they wish to use, and then input a value to convert.

menuOption = 0
print("1. Convert from Celsius to Fahrenheit")
print("2. Convert from Fahrenheit to Celsius")
print("Please select an option for the converter by selecting a number:")
menuOption = float(input())
print("")
if menuOption == 1:
	print("How many degrees in Celsius?")
	degreesCelsiusInput = float(input())
	degreesFahrenheitOutput = ((degreesCelsiusInput * 9) / 5) + 32
	print("")
	print(f"If the temperature is {degreesCelsiusInput} degrees Celsius, then the temperature in Fahrenheit is {round(degreesFahrenheitOutput, 1)} degrees.")
elif menuOption == 2:
	print("How many degrees in Fahrenheit?")
	degreesFahrenheitInput = float(input())
	degreesCelsiusOutput = ((degreesFahrenheitInput - 32) * 5) / 9
	print("")
	print(f"If the temperature is {degreesFahrenheitInput} degrees Fahrenheit, then the temperature in Celsius is {round(degreesCelsiusOutput, 1)} degrees.")
else:
	print("ERROR OCCURRED")
