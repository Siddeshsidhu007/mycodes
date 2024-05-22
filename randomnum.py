import random
import time

def get_valid_guess():
    
    while True:
        guess = input("Enter your guess (1-100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
        print("Please enter a valid number between 1 and 100.")

def play_game():
    
    number_to_guess = random.randint(1, 100)
    max_attempts = 6
    attempts_left = max_attempts

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 6 attempts to guess it. Let's begin!")
    time.sleep(1)

    while attempts_left > 0:
        guess = get_valid_guess()
        attempts_left -= 1

        if guess < number_to_guess:
            print("Too low! Try guessing a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} "
                  f"in {max_attempts - attempts_left} guesses!")
            return

    print(f"Sorry, the number I was thinking of was {number_to_guess}.")

def main():
    
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        play_game()
        play_again = input("Do you want to play again? (yes/no) ")

if __name__ == "__main__":
    main()
