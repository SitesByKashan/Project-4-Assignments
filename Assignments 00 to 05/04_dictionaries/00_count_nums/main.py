def count_number():
    print("Enter numbers one by one. Press Enter without typing anything to finish.\n")
    numbers = []
    
    while True:
        value = input("Enter a number: ")
        if value == "":
            break
        numbers.append(int(value))


    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    print("\nResults:")
    for num, count in count_dict.items():
        print(f"{num} appears {count} times.")


count_number()
