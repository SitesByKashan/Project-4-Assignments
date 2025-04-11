import random
from colorama import Fore, Style, init

init(autoreset=True)

def main():

    secret_number: int = random.randint(1, 99)
    
    print(Fore.CYAN + "I am thinking of a number between 1 and 99...")

    guess = int(input(Fore.YELLOW + "Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number: 
            print(Fore.RED + "Your guess is too low! 😟")
        else:
            print(Fore.RED + "Your guess is too high! 😟")
        print() 
        
        guess = int(input(Fore.YELLOW + "Enter a new guess: "))
    
    print(Fore.GREEN + Style.BRIGHT + "Congrats! 🎉 The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
