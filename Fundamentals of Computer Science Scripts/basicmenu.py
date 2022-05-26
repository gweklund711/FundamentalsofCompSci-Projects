# This is a script for a basic menu. Originally, I made this using while statements and switch statements in Swift.
# However, Python lacks switch statements, so I opted remade it with if/elif/else statements and a while statement
# for the menu.
menuOption = int(0)
while menuOption != 7:
    print("")
    print("Please select one of the options below:")
    print("1. Give you up")
    print("2. Let you down")
    print("3. Run around and desert you")
    print("4. Make you cry")
    print("5. Say goodbye")
    print("6. Tell a lie and hurt you")
    print("7. Quit")
    menuOption = int(input())

    if menuOption == 1:
        print("Never gonna give you up")
    elif menuOption == 2:
        print("Never gonna let you down")
    elif menuOption == 3:
        print("Never gonna run around and desert you")
    elif menuOption == 4:
        print("Never gonna make you cry")
    elif menuOption == 5:
        print("Never gonna say goodbye")
    elif menuOption == 6:
        print("Never gonna tell a lie and hurt you")
    elif menuOption == 7:
        print("PROGRAM ENDED")
    else:
        print("ERROR OCCURRED")