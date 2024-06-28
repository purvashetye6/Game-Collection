import random

print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 10. Can you guess it?")
print("You have 5 attempts. Let's begin!\n")

r = random.randint(0, 10)
no_of_guesses = 1

while no_of_guesses <= 5:
    user_input = int(input("Guess a number between 0 and 10: "))

    if user_input == r:
        print("\nCongratulations! You guessed it right!")
        break
    elif user_input < r:
        print("Make a bigger guess.")
    else:
        print("Make a smaller guess.")

    print("No. of guesses left:", 5 - no_of_guesses, "\n")
    no_of_guesses += 1

else:
    print("\nGame over. The number was:", r, "\n")

