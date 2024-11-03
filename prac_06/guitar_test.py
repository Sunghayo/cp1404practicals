"""
Estimated Time: 10 minutes
Start Time: 22:30
Actual Time: 22:40

Test program for Guitar class.
"""

from guitar import Guitar


def main():
    # Create guitar instances
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 825.45)

    # Test get_age() method
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 10. Got {another.get_age()}")

    # Test is_vintage() method
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

    # Additional test for 50-year threshold
    fifty_guitar = Guitar("50-year old guitar", 1973, 1234.56)
    print(f"\n{fifty_guitar.name} is_vintage() - Expected True. Got {fifty_guitar.is_vintage()}")


if __name__ == '__main__':
    main()