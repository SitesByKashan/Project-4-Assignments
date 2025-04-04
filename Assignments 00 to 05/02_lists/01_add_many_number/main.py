def sum_of_numbers(numbers):
    total_num: int = 0
    for number in numbers:
        total_num += number
    return total_num

numbers_list: list = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers_list)
print(f"The sum of the numbers is: {result}")
