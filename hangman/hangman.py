import random
def welcome_message():
    print("HANGMAN")
    print("Welcome to the Hangman game!")
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'

    return display
def play_game():
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 8

    print("Guess the word", display_word(secret_word, guessed_letters) + ":")

    while attempts_left > 0:
        guess = input(f"Input a letter (attempts left: {attempts_left}): > ").lower()

        if not guess.isalpha() or not guess.islower() or len(guess) != 1:
            print("You should input a single lowercase English letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("That letter doesn't appear in the word")
        else:
            print("No improvements")

        print(display_word(secret_word, guessed_letters))

        if display_word(secret_word, guessed_letters) == secret_word:
            print(f"You guessed the word {secret_word}!\nYou survived!")
            break

        attempts_left -= 1

        if attempts_left == 0:
            print(f"Thanks for playing!\nYou ran out of attempts. The correct word was: {secret_word}")
            break
def main_menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')

        if choice.lower() == 'play':
            play_game()
        elif choice.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'play' or 'exit'.")
if __name__ == "__main__":
    welcome_message()
    main_menu()
