print(r'''
  ____||____
 ///////////\
///////////  \
|    _    |  |
|[] | | []|[]|
|   | |   |  |
''')
print("Welcome to Treasure Chasm.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a chasm. '
                    'There is a house on the other side. '
                    'Type "wait" to wait for a helicopter. '
                    'Type "walk" to walk the tightrope across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the other side unharmed. "
                        "There is a house with 4 doors. One red, "
                        "one yellow, one blue, and one green. "
                        "Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over.")
        elif choice3 == "green":
            choice4 = input('You fall into a dark room. Do you shout for help or search for an exit? '
                            'Type "shout" to shout for help. '
                            'Type "search" to search for exit.\n').lower()
            if choice4 == "shout":
                print("You waste all of your energy before anyone hears you. Game over.")
            elif choice4 == "search":
                print("You escape the house with no treasure. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You fell into the abyss. Game over.")
else:
    print("You fell in a hole. Game over.")