"""
Adventure Game: Jungle Escape
This game includes at least three levels of choices, multiple options, and creative branching. 
Invalid responses are handled appropriately, and user input is case-insensitive.

Added creativity:
- A hidden option in the first level ("HELP") that gives hints.
- A fun storyline with unexpected twists.
- Enhanced input validation with retry attempts.
"""

def adventure_game():
    print("Welcome to the Jungle Escape!")
    print("You wake up in the middle of a dense jungle. You hear strange noises around you.")
    print("You have three choices: CLIMB a nearby tree to look around, WALK toward the sound of water, or CALL for help.")
    
    while True:
        choice1 = input("What do you do? (CLIMB/WALK/CALL/HELP): ").strip().lower()
        
        if choice1 == "climb":
            print("\nYou climb the tree and spot a waterfall in the distance.")
            print("Do you HEAD to the waterfall or SEARCH the tree for fruit?")
            
            while True:
                choice2 = input("What do you do? (HEAD/SEARCH): ").strip().lower()
                
                if choice2 == "head":
                    print("\nYou head toward the waterfall and find a hidden cave behind it.")
                    print("Do you ENTER the cave or RETURN to the jungle?")
                    
                    while True:
                        choice3 = input("What do you do? (ENTER/RETURN): ").strip().lower()
                        if choice3 == "enter":
                            print("\nInside the cave, you discover ancient treasure! You win!")
                            return
                        elif choice3 == "return":
                            print("\nYou return to the jungle and get lost. Game over.")
                            return
                        else:
                            print("\nInvalid choice. Try again.")
                elif choice2 == "search":
                    print("\nYou find delicious fruit in the tree, but also disturb a nest of angry birds!")
                    print("Do you FLEE or FIGHT?")
                    
                    while True:
                        choice3 = input("What do you do? (FLEE/FIGHT): ").strip().lower()
                        if choice3 == "flee":
                            print("\nYou escape the birds but fall from the tree. Game over.")
                            return
                        elif choice3 == "fight":
                            print("\nYou bravely fight off the birds and find a map hidden in the nest. You win!")
                            return
                        else:
                            print("\nInvalid choice. Try again.")
                else:
                    print("\nInvalid choice. Try again.")
        elif choice1 == "walk":
            print("\nYou walk toward the sound of water and find a river.")
            print("Do you SWIM across the river or FOLLOW it downstream?")
            
            while True:
                choice2 = input("What do you do? (SWIM/FOLLOW): ").strip().lower()
                if choice2 == "swim":
                    print("\nYou swim across the river but encounter crocodiles. Game over.")
                    return
                elif choice2 == "follow":
                    print("\nYou follow the river and discover a friendly tribe who helps you escape. You win!")
                    return
                else:
                    print("\nInvalid choice. Try again.")
        elif choice1 == "call":
            print("\nYou call for help, and surprisingly, someone responds!")
            print("Do you RUN toward the voice or HIDE to see who it is?")
            
            while True:
                choice2 = input("What do you do? (RUN/HIDE): ").strip().lower()
                if choice2 == "run":
                    print("\nYou run toward the voice and find a rescue team! You win!")
                    return
                elif choice2 == "hide":
                    print("\nYou hide and realize it's a trap set by hunters. Game over.")
                    return
                else:
                    print("\nInvalid choice. Try again.")
        elif choice1 == "help":
            print("\nHint: Choose wisely and pay attention to your surroundings!")
        else:
            print("\nInvalid choice. Try again.")

# Run the game
adventure_game()

# Prevent the terminal from closing immediately after the game ends
input("\nPress Enter to exit...")