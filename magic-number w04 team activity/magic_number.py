import random  # Import the random library to generate a random number

# Main game loop
play_again = "yes"

while play_again.lower() == "yes":
    magic_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    guess = -1  # Initialize the guess variable
    attempts = 0  # Counter to track the number of attempts

    print("\nWelcome to the Guess My Number Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while guess != magic_number:
        # Ask the user for a guess
        guess = int(input("What is your guess? "))
        attempts += 1  # Increment the attempt counter

        # Check if the guess is lower, higher, or correct
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")

print("Thank you for playing! Goodbye!")
