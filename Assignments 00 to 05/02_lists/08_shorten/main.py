MAX_LENGTH = 3

def shorten(lst):
    if len(lst) <= MAX_LENGTH:
        return 

    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  
        print(f"Removed: {removed_item}")

def main():
    lst = [1, 2, 3, 4, 5]
    
    print(f"Original list: {lst}")
    shorten(lst)
    print(f"List after shortening: {lst}")


main()
