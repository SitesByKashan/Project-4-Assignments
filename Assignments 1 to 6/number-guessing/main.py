import random
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
if difficulty == "easy":
    rannum = random.randint(1, 20)  
    attempts = 10
    print("I'm thinking of a number between 1 to 20.")
elif difficulty == "hard":
    rannum = random.randint(1, 50)
    attempts = 5
    print("I'm thinking of a number between 1 to 50.")
else:
    print("Invalid difficulty choice. Please restart the game and choose 'easy' or 'hard'.")
    exit()
while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")

    guess = input("Make a guess: ").strip()
    
    if not guess.isdigit():  # Check if input is a number
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    if guess < rannum:
        print("Too low.")
    elif guess > rannum:
        print("Too high.")
    else:
        print(f"🎉 You got it! The answer was {rannum}.")
        break

    attempts -= 1

    if attempts == 0:
        print(f"😢 You've run out of guesses. The number was {rannum}. You lose.")
    else:
        print("Guess again!")