import random

options = ("rock", "paper", "scissors")

computer_score = 0
user_score = 0

while True:

    if computer_score == 3 or user_score == 3:
        break

    computer_choice = random.choice(options)

    user_choice = input("Enter your choice (Rock/Paper/Scissors/Quit): ").lower()

    if user_choice =="quit":
        break

    if user_choice not in options:
        print("\nInvalid choice. Please choose from Rock, Paper, Scissors, or Quit.\n")
        continue

    print("Computer: ", computer_choice, "\n")

    if user_choice == computer_choice:
        print("Tie")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win")
        user_score +=1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win")
        user_score +=1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win")
        user_score +=1

    else:
        print("Computer wins")
        computer_score += 1

    print("User Score: ", user_score)
    print("Computer Score: ", computer_score, "\n")

if user_score == 3:
    print("Congratulations! You are the WINNER!")
elif computer_score == 3:
    print("Sorry, Computer is the WINNER!")

print("Thanks for PLaying\n")
