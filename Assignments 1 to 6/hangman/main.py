import random

words = ["python", "developer", "hangman", "programming", "computer", "science"]

word = random.choice(words)
word_letters = set(word) 
guessed_letters = set() 
attempts = 6 

print("🎭 Welcome to Hangman! Can you guess the word? 🔤")

while attempts > 0 and word_letters:

    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

    guess = input("🔤 Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter! Try again.")
    elif guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempts left.")

        hangman_stages = [
            "  😵💀  ",   
            "  😨|   ",   
            "  😰/|  ",   
            "  🥶/|\\ ",  
            "  🫣/|\\ ",  
            "  😱/|\\ /  " 
        ]
        if attempts < 6:
            print(hangman_stages[5 - attempts])  

if not word_letters:
    print(f"🎉 Congratulations! You guessed the word: {word.upper()} 🏆")
else:
    print(f"💀 Game Over! The correct word was: {word.upper()}")
