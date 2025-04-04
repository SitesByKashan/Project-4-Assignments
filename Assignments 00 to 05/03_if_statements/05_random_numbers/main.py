import random

def print_random_numbers():
    for i in range(10):
        value = random.randint(1, 100)
        print(value, end=" ")
    print()  

print_random_numbers()
