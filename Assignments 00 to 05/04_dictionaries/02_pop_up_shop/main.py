def fruit_shop():
    fruit_prices = {
        "apple" : 3.0,
        "durian" : 15.5,
        "jackfruit" : 8.0,
        "kiwi" : 2.5,
        "rambutan" : 4.0,
        "mango" : 5.0
    }

    total_cost = 0
    print("Welcome To Our Fruit Shop!\n")
    for fruit, price in fruit_prices.items():
        while True:
            quantity = input(f"How many ({fruit}) do you want?: ")
            quantity = int(quantity)
            if quantity < 0:
                print("Please Enter a Non-Zero Number...")
            else:
                break
        total_cost += quantity * price
    print(f"Your total is ${total_cost:.2f}")

fruit_shop()
                