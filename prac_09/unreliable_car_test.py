"""
CP1404/CP5632 Practical
UnreliableCar Test Program
"""
from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar."""
    # Create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # Attempt to drive both cars multiple times
    for i in range(1, 12):
        print(f"\nAttempting to drive {i}0km:")
        print(f"{good_car.name:12} drove {good_car.drive(i * 10):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i * 10):2}km")

    # Print final states of the cars
    print(f"\n{good_car}")
    print(f"{bad_car}")


main()