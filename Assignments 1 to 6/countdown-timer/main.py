import time
from colorama import Fore, Style, init

init(autoreset=True)

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{Fore.CYAN}{mins:02d}:{secs:02d}{Style.RESET_ALL}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print(Fore.BLUE + "🚀 Time's up! 🚀" + Style.RESET_ALL)

t = input(Fore.MAGENTA + "Enter the time in seconds: " + Style.RESET_ALL)
countdown_timer(int(t))
