print(r'''
                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'

''')

print("Welcome to Lake Crossing.")
print("Your mission is to make it to the other side of the lake.")

choice1 = input('You\'re debating whether to take the jet ski or swim across.\nType "j" to take the jet ski. Type "s" to swim across.\n').lower()

if choice1 == "j":
    choice2 = input('You run out of gas. You can either wait for help or swim back to shore.\nType "h" to wait for help. Type "s" to swim back to shore.\n').lower()
    if choice2 == "h":
        choice3 = input('Three people offer assistance. One has a catamaran. The second has a sailboat. The third has a jet ski.\nType "c" to hop on the catamaran. Type "s" to hop on the sailboat. Type "j" to hop on the jet ski.\n').lower()
        if choice3 == "c":
            print("Congrats! You made it safely to the other side.")
        elif choice3 == "s":
            print("The sailboat capsized, taking you down with it. Game Over.")
        else:
            print("You fell off the jet ski and drowned. Game Over.")
    else:
        print("You ran out of energy and drowned. Game Over.")
else:
    print("You ran out of energy and drowned. Game Over.")