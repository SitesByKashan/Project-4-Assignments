def double_until_100():
   while True:
    current_value = input("Enter a Number: ") 
    current_value = int(current_value)
    if current_value >= 100:
        print("Please enter a value which is less then 100...")
    else:
       break

   while current_value < 100:
        current_value *= 2
        print(current_value, end =" ")


double_until_100()
   