def computer_guesses():
    print("🤖 Let's play 'Guess Your Number'!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("After each guess, tell me:")
    print("'h' if my guess is too high")
    print("'l' if my guess is too low")
    print("'c' if I guessed correctly")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nIs your number {guess}?")
        feedback = input("Enter (h/l/c): ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Computer guessed the number {guess} correct in {attempts} tries.")
            return
        else:
            print("❌ Invalid input. Please enter 'h', 'l', or 'c'.")

    print("Hmm 🤔 something went wrong. Are you sure you were honest? 😅")

# Run the game
if __name__ == "__main__":
    computer_guesses()
