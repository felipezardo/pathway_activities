
# This program is a word guessing game where the secret word is randomly selected from a list. 
# The player receives hints showing correctly placed letters in uppercase, misplaced letters in lowercase, and incorrect letters as underscores.
# Additionally, the game keeps track of the words that have already been guessed, ensuring that no word is repeated during the session.


import random

def generate_hint(secret_word, guess):
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # Correct letter in correct position
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  # Correct letter in wrong position
        else:
            hint.append("_")  # Incorrect letter
    return " ".join(hint)

def word_puzzle_game():
    word_list = ["mosiah", "lehi", "nephi", "helaman", "moroni"]
    used_words = set()
    
    while True:
        if len(used_words) == len(word_list):
            print("You've guessed all available words! Thanks for playing!")
            input("Press Enter to exit...")
            break
        
        available_words = list(set(word_list) - used_words)
        secret_word = random.choice(available_words)  # Randomly selecting a new secret word
        used_words.add(secret_word)
        attempts = 0
        
        print("Welcome to the word guessing game!\n")
        print("Your hint is:", "_ " * len(secret_word))
        
        while True:
            guess = input("What is your guess? ").strip().lower()
            attempts += 1
            
            if len(guess) != len(secret_word):
                print("Sorry, the guess must have the same number of letters as the secret word.")
                continue
            
            if guess == secret_word:
                print("Congratulations! You guessed it!")
                print(f"It took you {attempts} guesses.")
                break
            
            print("Your hint is:", generate_hint(secret_word, guess))
        
        if len(used_words) == len(word_list):
            print("You've guessed all available words! Thanks for playing!")
            input("Press Enter to exit...")
            break
        
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Invalid response. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    word_puzzle_game()
