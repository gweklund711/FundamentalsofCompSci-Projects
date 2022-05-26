import random
# This was a major assignment that I worked on for about a week of class time.
# Basically, I had to design a menu with different functions for each of the options.
# However, since I used Swift to design it, the project contained switch statements to
# make the menu infinitely repeat until the user ended the program. But Python lacks
# a simple switch statement feature. So, the menu  is made with if statements instead.
# In theory, I could combine all of my projects into this one script. However, doing that
# would make it harder for a person to view the individual projects.
print("Welcome to my menu project!")
print("This project contains 5 basic options for you to interact with.")
print("So, go ahead. Select one of the options below by typing in the number.")
menuOption = int(0)
while menuOption != 6:
    print("1. Play a card game")
    print("2. Use a calculator")
    print("3. Find the largest number in an array")
    print("4. Determine if a word is a palindrome")
    print("5. Break the console")
    print("6. Quit")
    menuOption = int(input())
    print("")

    if menuOption == 1:
        print("Welcome to the Card Game!")
        print("What is the first player's name?")
        userOne = input()
        print("What is the second player's name?")
        userTwo = input()
        print("How many turns do you want to play for? (enter a number)")
        turnValue = int(input())
        for i in range(1, (turnValue)):
            cardOne = random.randint(1, 13)
            print(f"{userOne}'s card is {cardOne}")
            cardTwo = random.randint(1, 13)
            print(f"{userTwo}'s card is {cardTwo}.")
            if cardOne > cardTwo:
                print(f"{userOne} WINS")
                print(f"{userTwo} LOSES")
                print("")
            elif cardTwo > cardOne:
                print(f"{userTwo} WINS")
                print(f"{userOne} LOSES")
                print("")
            else:
                print(f"{userOne} and {userTwo} TIED.")
                print("")

    if menuOption == 2:
        print("Welcome to the Calculator!")
        print("Please input the first number here:")
        numOne = float(input())
        print("Please input the second number here:")
        numTwo = float(input())
        print("")


        def addNums():
            numSum = round((numOne + numTwo), 1)
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
        print("")

    if menuOption == 3:
        print("Welcome to the Largest Number Calculator!")
        print("You can't do anything here, but you should still watch this!")
        epicArray = [3, 27, 89, 19, 21, 52]
        largestNum = int(max(epicArray))
        print(f"In the array of {epicArray}, the largest number is {largestNum}.")

    if menuOption == 4:
        print("Welcome to the Palindrome Calculator!")
        print("Type in a word:")
        wordOriginal = input()
        wordReversed = wordOriginal[::-1]
        if wordOriginal == wordReversed:
            print(f"{wordOriginal} is a palindrome.")
            print("")
        else:
            print(f"{wordOriginal} is not a palindrome.")
            print("")

    if menuOption == 5:
        print("Welcome to the Console Destroyer")
        infinity = int(0)
        while infinity != 1:
            print("Gunnar in Norse mythology, son of King Giuki and Queen Grimhild of the Nibelungs, or Burgundians, brother of the beautiful Gudrun and the warrior Hogni. Assisted by an unwitting Sigurd, Gunnar won the warrior maiden Brynhild for his wife through trickery. He and Sigurd had sworn an oath of brotherhood. Gunnar later conspired in the murder of Sigurd, and was himself slain at the court of King Atli of the Huns. Brynhild, a powerful Valkyrie, was to marry only the most valiant warrior; she lay sleeping encircled by a magical ring of fire. Gunnar and his horse, Goti, were unable to traverse the flames, so Sigurd and his horse, Grani, exchanged forms and names with Gunnar and Goti, and rode through the flames without hesitation. Brynhild believed Gunnar was worthy of her hand, and she consented to marriage. Upon her marriage, Brynhild lost her supernatural powers and unhappily resigned herself to her union with Gunnar. When she discovered how she had been deceived, however, her smoldering resentment became outright hatred directed against Sigurd, the only warrior truly worthy of her hand. In one version of the myth, she instigated Gunnar and Hogni against Sigurd; in another variation, Gunnar himself was so jealous of Sigurd that he participated in the plot to kill his oath-brother. After Sigurd’s murder, Brynhild killed herself. Sigurd’s widow, Gudrun, married King Atli of the Huns. Atli demanded that Gunnar and Hogni relinquish the Nibelung treasure, which they had hid. The brothers refused to give up the treasure, which Sigurd had won from the dragon Fafnir. In retaliation, Atli had Hogni’s heart cut out, and then had Gunnar thrown into a snake pit to die in agony. Gunnar attempted to charm the snakes with a harp, but one adder resisted the enchantment and fatally bit him. In the Germanic epic ‘Song of the Nibelungs’ (Nibelungenlied), Gunnar is called Gunther.")

    if menuOption == 6:
        print("PROGRAM ENDED")


    else:
        print("")