import random

gameValue = ["rock", "paper", "scissor"]
print("Welcome to the Rock - Paper - Scissor Game")
user_Choice = input(
    "Enter your choice (rock, paper, or scissors): ").strip().lower()
if user_Choice in gameValue:
    computer_Choice = gameValue[random.randint(0, 2)]
    if (computer_Choice == user_Choice):
        print(f"Computer Choice : {computer_Choice} ")
        print(f"Match Tie")

    elif (computer_Choice == "paper" and user_Choice == "scissor"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Scissors beats Paper (Scissors cut Paper)")

    elif (computer_Choice == "rock" and user_Choice == "paper"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Paper beats Rock (Paper covers Rock)")

    elif (computer_Choice == "rock" and user_Choice == "scissor"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Rock beats Scissors (Rock crushes Scissors)")

    elif (computer_Choice == "scissor" and user_Choice == "paper"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Scissors beats Paper (Scissors cut Paper)")

    elif (computer_Choice == "scissor" and user_Choice == "rock"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Rock beats Scissors (Rock crushes Scissors)")

    elif (computer_Choice == "paper" and user_Choice == "rock"):
        print(f"Computer Choice : {computer_Choice}")
        print(f"Paper beats Rock (Paper covers Rock)")

else:
    print("Invalid Input try again")
