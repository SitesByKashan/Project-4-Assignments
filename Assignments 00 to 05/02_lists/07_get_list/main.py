def get_list():
    print("This program can add numbers to the list. Press Enter without typing anything to print the list.")
    values = []
    
    while True:
        value = input("Enter the value to add to your list: ")
        if value == "":
            break

        value = int(value)
        values.append(value)

    
    print(f"Here is the complete list: {values}")

get_list()
