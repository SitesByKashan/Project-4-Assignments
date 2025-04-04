def tall_enough_to_ride():
    while True:
        height = input("How tall are you? ")
        if height == "":
            print("Goodbye!")
            break
        height = int(height)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

tall_enough_to_ride()
