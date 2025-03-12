import random

def main():
    words = ["python", "javascript", "hangman", "programming", "computer", "gaming", "keyboard"]
    
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    word = random.choice(words).lower()
    guessed_letters = set()
    max_wrong_guesses = len(hangman_stages) - 1
    wrong_guesses = 0
    display_word = ["_"] * len(word)

    print("Welcome to Hangman!")
    
    while wrong_guesses < max_wrong_guesses:
        print(hangman_stages[wrong_guesses])
        print("Word:", " ".join(display_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
            if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                return
        else:
            wrong_guesses += 1
            print("Wrong guess!")
    
    print(hangman_stages[wrong_guesses])
    print("Game over! The word was:", word)

if __name__ == "__main__":
    main()
