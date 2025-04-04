def fahrenheit_to_celsius():
    print("This Program can convert temperature fahrenheit to celsius")
    fahrenheit : str = input("Enter your fahrenheit temperature: ")
    fahrenheit = float(fahrenheit)
    celsius : float = (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")

fahrenheit_to_celsius()