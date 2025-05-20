import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("🎮 Let's play Rock, Paper, Scissors!")

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! 👋")
            break

        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie! 😐")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win! 🎉")
        else:
            print("You lose! 😢")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()