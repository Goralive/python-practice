from guess_game import randrange


def guessing_game():
    # Generate a random number between 0 and 10
    target_number = randrange(10)
    # Prompt the user to guess the number
    while True:
        try:
            guess = int(input("Guess the number between 0 and 10: "))
            if guess < 0 or guess > 10:
                print("Please enter a number between 0 and 10.")
                continue

            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Incorrect guess. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Start the game
guessing_game()
