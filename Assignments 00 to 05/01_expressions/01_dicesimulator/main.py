import random

def roll_dice():
    """Simulates rolling two dice and prints the results."""
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6) 
    print(f"Die 1: {die1}, Die 2: {die2}") 
    total: int = die1 + die2
    print("Total of two dice:", total) 

def main():
    print("Rolling two dice three times...")
    roll_dice()
    roll_dice()
    roll_dice()

main()
