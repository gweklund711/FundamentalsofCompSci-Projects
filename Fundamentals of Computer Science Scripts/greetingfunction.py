# This script reads in the inputted name from the user and then uses a simple function to greet said user.
print("What is your name?")
userName = input()
def greetUser():
    userGreeting = "Hello," + userName + "!"
    return userGreeting
print(greetUser())