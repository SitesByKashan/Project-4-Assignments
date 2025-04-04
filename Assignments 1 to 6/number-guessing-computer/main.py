import random

def computer_guess(low, high):
    attempts = 0
    while low <= high:
        attempts += 1
        guess = random.randint(low, high)
        print(f"Computer guesses: {guess}")
        
        user_feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").strip().lower()
        
        if user_feedback == "c":
            print(f"🎉 Computer guessed the number {guess} correctly in {attempts} attempts!")
            break
        elif user_feedback == "h":
            high = guess - 1
        elif user_feedback == "l":
            low = guess + 1 
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    
    if low > high:
        print("Something went wrong! Did you give the wrong hints? 😅")

print("Think of a number between 1 and 100, and I'll try to guess it!")
input("Press Enter when you're ready...") 
computer_guess(1, 100)
