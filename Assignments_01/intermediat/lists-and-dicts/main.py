def list_practice():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print(f"Length of the list: {len(fruit_list)}")
    
    fruit_list.append('mango')
    
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index is out of range"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index is out of range"

def slice_list(lst, start_index, end_index):
    if 0 <= start_index < len(lst) and 0 <= end_index <= len(lst):
        return lst[start_index:end_index]
    else:
        return "Invalid indices"

def index_game():
    game_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter the operation number: ")

        if choice == '1':
            index = int(input("Enter the index of the element to access: "))
            print("Element:", access_element(game_list, index))
        
        elif choice == '2':
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            print("Updated list:", modify_element(game_list, index, new_value))
        
        elif choice == '3':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            print("Sliced list:", slice_list(game_list, start_index, end_index))
        
        elif choice == '4':
            print("Exiting game.")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Problem #1: List Practice\n")
    list_practice()

    print("\nNow let's practice with Problem #2: Index Game\n")

    index_game()

if __name__ == "__main__":
    main()