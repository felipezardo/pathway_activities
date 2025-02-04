# Mad Libs Game: Create your own story by providing words!

# Prompt the user for words
print("Welcome to the Mad Libs game! Please provide the following words:")

adjective = input("Adjective: ").strip()
animal = input("Animal: ").strip()
verb1 = input("Verb: ").strip()
exclamation = input("Exclamation: ").strip().capitalize()  # Automatically capitalizes the first letter
verb2 = input("Another verb: ").strip()
verb3 = input("One more verb: ").strip()

# Default story with placeholders filled by user input
story = f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.
"""

# Display the story
print("\nHere is your story:")
print(story)

# Extra story themes
print("\nWould you like to create another story with a different theme? Choose:")
print("1. Adventure Story")
print("2. Horror Story")
choice = input("Enter the number of your choice (or press Enter to exit): ").strip()

if choice == "1":
    # Adventure story
    place = input("Place: ").strip()
    weapon = input("Weapon: ").strip()
    hero = input("Hero's name: ").strip()

    adventure_story = f"""
    One day, {hero} was exploring the mysterious {place}. Suddenly, a {adjective} {animal} appeared, 
    ready to attack. With quick thinking, {hero} grabbed a {weapon} and began to {verb1}. 
    "{exclamation}!" echoed through the {place} as the {animal} finally retreated. It was a victory to remember!
    """
    print("\nHere is your adventure story:")
    print(adventure_story)

elif choice == "2":
    # Horror story
    sound = input("Scary sound: ").strip()
    object = input("Strange object: ").strip()
    fear = input("Biggest fear: ").strip()

    horror_story = f"""
    It was a dark and stormy night. The sound of {sound} filled the air, and I knew something was wrong.
    When I turned around, I saw a {adjective} {animal} holding a {object}. 
    "{exclamation}!" I screamed, running away. But no matter where I went, the fear of {fear} haunted me forever.
    """
    print("\nHere is your horror story:")
    print(horror_story)

else:
    print("\nThank you for playing! See you next time.")
