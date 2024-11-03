"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Create my_car instance with initial fuel of 180
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 1. Create a new Car object called "limo" with 100 units of fuel
    limo = Car(100, "Limo")

    # 2. Add 20 more units of fuel to limo
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # 4. Attempt to drive the car 115 km
    limo.drive(115)

    # 7. Print the car objects to test the __str__ method
    print("\nTesting __str__ method:")
    print(my_car)
    print(limo)


main()