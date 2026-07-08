# HANGMAN GAME

import random
print("=== HANGMAN GAME ===")

words=["apple","banana","carrot","dog","elephant","python","computer", "github", "coding"]
secret_word=random.choice(words)

lives = 6

display=[]
for letters in secret_word:
    display.append("_")
    

while "_" in display and lives > 0:
    
    print("\nGuess the word:")

    for letters in display:
        print(letters,end="")
    print()
    
    print(f"\nLives Remaining: {lives}")

    guess = input("\nGuess a letter: ").lower()

    if guess in secret_word:

        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display[position] = guess

        print("\n✅ Correct!")

    else:
        lives -= 1
        print("\n❌ Wrong Guess!")


if "_" not in display:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", secret_word)

else:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)