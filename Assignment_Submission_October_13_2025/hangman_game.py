import random

def hangman():
    # Step 1: Define fruits and hints
    fruits_with_hints = {
        "apple": "A red or green fruit that keeps the doctor away",
        "banana": "A long yellow fruit loved by monkeys",
        "mango": "The king of fruits",
        "strawberry": "A red fruit with tiny seeds on its skin",
        "watermelon": "A large green fruit with red juicy flesh",
        "orange": "A citrus fruit rich in vitamin C",
        "grape": "Tiny round fruits that can make wine",
        "pineapple": "A tropical fruit with spiky skin",
        "cherry": "A small red fruit often seen on cakes",
        "kiwi": "A brown fruit with green flesh and tiny black seeds"
    }

    # Step 2: Randomly choose one fruit and its hint
    chosen_word, hint = random.choice(list(fruits_with_hints.items()))
    word_length = len(chosen_word)
    guessed_letters = []
    attempts = 6  # lives

    # Step 3: Create blanks for unguessed letters
    display = ["_"] * word_length
    print("Welcome to Fruit Hangman!")
    print(f"Hint: {hint}")
    print(f"The fruit name has {word_length} letters.")
    print(" ".join(display))

    # Step 4: Game loop
    while attempts > 0 and "_" in display:
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(f" You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # Step 5: Check guess
        if guess in chosen_word:
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f" Wrong! You have {attempts} lives left.")

        print(" ".join(display))
        print(f"Guessed so far: {', '.join(guessed_letters)}")

    # Step 6: Game result
    if "_" not in display:
        print(f" You guessed it right! The fruit was '{chosen_word}'.")
    else:
        print(f"Out of lives! The fruit was '{chosen_word}'. Better luck next time!")

# Run the game
hangman()