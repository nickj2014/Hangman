import random


def main():
    print("Welcome to hangman!")
    word, guesses_left, guessed_letters, current_total = reset()  # Get initial values
    run = True

    while run:
        if check_outcome(current_total, word, guesses_left):  # Check if word guessed or ran out of lives
            run = replay()  # Check if user wants another game
            if run:
                word, guesses_left, guessed_letters, current_total = reset()  # Reset values
            else:
                break  # Quit
        else:  # If game not ended
            guess = input("\nGuess a letter: ")  # Get letter input, convert to upper for checking
            guess = guess.upper()
            if not valid_guess(guess, guessed_letters):  # Check if valid guess
                continue
            else:  # If valid guess, check if letter is in word
                guesses_left = check_letter(guess, current_total, word, guesses_left)  # Update remaining guesses
                print_row(current_total)  # Print updated row


def get_word():  # Imports sowpods.txt, pick random word stripping newline from end
    with open("txt files/sowpods.txt", "r") as infile:
        words = list(infile)
    word = random.choice(words).strip()
    return word


def print_row(current_total):  # Print out current total list as joined string
    print("")
    print("".join(current_total))


def valid_guess(guess, guessed_letters):  # Check guess validity
    if len(guess) > 1:  # Check if one character has been entered
        print("One letter at a time!")
        return False
    elif not guess.isupper():  # Check character is alphabet character
        print("Only alphabet characters allowed!")
        return False
    elif guess in guessed_letters:  # Check if already guessed
        print(f"You have already guessed {guess}.")
        return False
    else:
        guessed_letters.append(guess)  # If all good, append guess to guessed list
        return True


def check_letter(guess, current_total, word, guesses_left):  # Check if guess is in the word
    in_word = False  # Used to print out if letter was found in word
    for i in range(len(word)):  # Loop through length of word checking if guess matches each character
        if guess in word[i]:
            current_total[i] = guess  # If guess matches update current_total index to guess
            in_word = True
    if in_word:  # Don't remove life as correct guess
        print(f"\n{guess} is in the word! {guesses_left} guesses remaining.")
        print_man(guesses_left)  # Print hangman
        return guesses_left
    else:  # Remove life as incorrect guess
        guesses_left -= 1
        print(f"\n{guess} is not in the word. {guesses_left} guesses remaining.")
        print_man(guesses_left)  # Print hangman
        return guesses_left


def check_outcome(current_total, word, guesses_left):  # Check if current_total joined as string matches word string
    if "".join(current_total) == word:
        print("\nYou won!")
        return True
    elif guesses_left == 0:  # Check if run out of guesses
        print("\nYou ran out of lives!")
        print(f"The word was {word}.")
        return True
    return False


def reset():  # Contains the initial values for each variable
    word = get_word()  # Get random word
    guessed_letters = []  # Empty list of letters
    guesses_left = 6  # Guesses remaining
    current_total = "_" * len(word)  # Generate lines for length of word, convert to list to iterate later
    current_total = list(current_total)
    print_row(current_total)  # Print empty lines
    return word, guesses_left, guessed_letters, current_total


def replay():  # Check if user wants another game
    choice = input("Another game? Y/N: ")
    if choice.upper() in ["Y", "YES"]:
        return True
    else:
        print("Goodbye!")
        return False


def print_man(guesses_remaining):
    if guesses_remaining == 5:
        print("_____")
        print("|   |")
        print("|   O")
        print("|")
        print("|")
        print("|_______ ")
    elif guesses_remaining == 4:
        print("_____")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|")
        print("|_______ ")
    elif guesses_remaining == 3:
        print("_____")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|  / ")
        print("|_______ ")
    elif guesses_remaining == 2:
        print("_____")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|  / \\")
        print("|_______ ")
    elif guesses_remaining == 1:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  ~|")
        print("|  / \\")
        print("|_______ ")
    elif guesses_remaining == 0:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  ~|~")
        print("|  / \\")
        print("|_______ ")


main()
