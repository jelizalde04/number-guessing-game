import random

def guess_number():
    # The server chooses a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 3  # Limit to 3 attempts

    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            # The player enters a number
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Correct! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts.")
                break  # The game ends when the number is guessed
        except ValueError:
            print("Please enter a valid number.")
        
        # If the player has reached the maximum number of attempts
        if attempts == max_attempts:
            print(f"Sorry, you've used up your {max_attempts} attempts. The correct number was {number_to_guess}.")

# Call the main game function
if __name__ == "__main__":
    guess_number()
