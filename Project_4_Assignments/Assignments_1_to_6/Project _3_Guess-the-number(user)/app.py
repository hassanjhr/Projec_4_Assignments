import random

def user_guesses():
    print("🎲 I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! 🔽")
            elif guess > number:
                print("Too high! 🔼")
            else:
                print(f"🎉 You guessed the number {number} in {attempts} tries!")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    user_guesses()
