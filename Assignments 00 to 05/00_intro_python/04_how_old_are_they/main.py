def age():
    anton_age : int = 21
    beth_age : int = anton_age + 6
    chen_age : int = beth_age + 20
    drew_age : int = chen_age + anton_age
    ethan_age : int = chen_age

    print(f"Anton is {anton_age} years old.")
    print(f"Beth is {beth_age} years old.")
    print(f"Chen is {chen_age} years old.")
    print(f"Drew is {drew_age} years old.")
    print(f"Ethan is {ethan_age} years old.")
age()