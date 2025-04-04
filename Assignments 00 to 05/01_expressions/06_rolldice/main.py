import random

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}")
    print(f"Total: {total}")


roll_two_dice()
