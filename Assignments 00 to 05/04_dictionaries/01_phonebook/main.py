def phonebook_app():
    print("Welcome to the Phonebook App!")
    phonebook = {}

    while True:
        print("\nOptions:")
        print("1. Add a contact")
        print("2. Look up a contact")
        print("3. View all contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter the name: ")
            number = input("Enter the phone number: ")
            phonebook[name] = number
            print(f"Contact '{name}' added.")

        elif choice == "2":
            name = input("Enter the name to look up: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print("Contact not found.")

        elif choice == "3":
            if not phonebook:
                print("Phonebook is empty.")
            else:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


phonebook_app()
