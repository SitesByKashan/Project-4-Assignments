
def calculate_mars_weight():
    weight_on_earth = float(input("Enter a weight on Earth: "))

    weight_on_mars = weight_on_earth * 0.378

    print(f"The equivalent on Mars: {round(weight_on_mars, 2)}")
def planetary_weight():
    planet_gravity = {
        'Mercury': 0.376,
        'Venus': 0.889,
        'Mars': 0.378,
        'Jupiter': 2.360,
        'Saturn': 1.081,
        'Uranus': 0.815,
        'Neptune': 1.140
    }
    
    weight_on_earth = float(input("Enter a weight on Earth: "))

    planet = input("Enter a planet: ")

    planet = planet.title()

    if planet in planet_gravity:
        weight_on_planet = weight_on_earth * planet_gravity[planet]
        print(f"The equivalent weight on {planet}: {round(weight_on_planet, 2)}")
    else:
        print("Sorry, the planet is not recognized.")
def main():
    calculate_mars_weight()

    print("\nNow let's calculate your weight on other planets.\n")

    planetary_weight()
if __name__ == "__main__":
    main()
