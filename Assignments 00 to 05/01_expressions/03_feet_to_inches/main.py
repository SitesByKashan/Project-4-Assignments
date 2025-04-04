def feet_into_inches():
    INCHES_PER_FOOT = 12

    feet = float(input("Enter length in feet: "))

    inches = feet * INCHES_PER_FOOT

    unit = "foot" if feet == 1 else "feet"

    print(f"{feet} {unit} is {inches} inches.")

feet_into_inches()
