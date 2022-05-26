# This program loops through 1-100, and prints a specific phrase depending on certain conditions
# If the program detects a number to be a multiple of 3, it prints "Fizz"
# If the program detects a number to be a multiple of 5, it prints "Buzz"
# If the program detects a number to be a multiple of 3 AND 5, it prints "FizzBuzz"
# If the program detects that a number isn't a multiple of either 3 or 5, it simply prints the number

def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return 'FizzBuzz'

    elif number % 3 == 0:
        return 'Fizz'

    elif number % 5==0:
        return 'Buzz'
    else:
        return number

for n in range(1,100):
    print(fizz_buzz(n))