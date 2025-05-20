import random

def hangman():
    words = ["python", "hangman", "coding", "program", "developer"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman!")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! You have {attempts} tries left.")

        print("Word:", " ".join(guessed))

    if "_" not in guessed:
        print(f"🎉 Congratulations! You guessed the word '{word}'!")
    else:
        print(f"💀 Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
