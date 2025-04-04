#speed of light 
c = 299792458

def mass_into_energy():
    print("This program convert mass into energy")
    mass : str = input("Enter your body mass in kg: ")
    mass = float(mass)
    energy = mass * (c ** 2)
    print("e = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {c} m/s")
    
    print(f"{energy} joules of energy!")

mass_into_energy()
    