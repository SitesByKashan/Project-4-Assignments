def affirmation_checker():
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        user_input = input("Please type the following affirmation: ")
        if user_input == affirmation:
            print("That's right! :)")
            break 
        else:
            print("Hmmm, that was not the affirmation. Try again.")


affirmation_checker()
