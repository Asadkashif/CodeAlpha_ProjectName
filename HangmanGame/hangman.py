import random
from words import word_list

def choose_word():
    """Select a random word from the word list"""
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters"""
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)

def hangman():
    """Main game function"""
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.\n")
    
    # Initialize game variables
    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    
    while incorrect_guesses < max_attempts:
        # Display current game state
        print("\n" + display_word(word_to_guess, guessed_letters))
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        
        # Get player input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
            
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_to_guess:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_attempts - incorrect_guesses} guesses left.")
        
        # Check if player has won
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    
    # If player runs out of guesses
    if incorrect_guesses == max_attempts:
        print("\nGame over! You ran out of guesses.")
        print("The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()