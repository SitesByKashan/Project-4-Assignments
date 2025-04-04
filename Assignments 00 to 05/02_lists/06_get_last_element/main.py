def get_first_element(lst):
    """Print the first element of the list."""
    last_element = lst.pop()
    print(last_element)

def main():
    n = int(input("Enter the number of elements in the list: "))
    user_list = []
    
    for i in range(n):
        element = input("Enter an element: ")
        user_list.append(element)
    get_first_element(user_list)

main()
