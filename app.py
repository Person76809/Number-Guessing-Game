import random

# Define the game function
def guess_number():
    # Generate a random number between 1 and 20
    number = random.randint(1, 20)
    
    # Allow the player to guess up to 6 times
    for i in range(6):
        # Ask the player to guess the number
        guess = int(input("Guess a number between 1 and 20: "))
        
        # Check if the guess is correct
        if guess == number:
            print("Congratulations! You guessed the number.")
            return
        
        # Give a hint if the guess is too high or too low
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    
    # If the player runs out of guesses, reveal the number
    print("Sorry, you ran out of guesses. The number was", number)

# Call the game function
guess_number()

