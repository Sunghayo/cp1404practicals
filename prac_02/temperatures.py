# Constants for menu options and temperature conversion factors
MENU = """C - Convert Celsius to Fahrenheit F - Convert Fahrenheit to Celsius Q - Quit"""
FAHRENHEIT_MULTIPLIER = 9.0 / 5
FAHRENHEIT_OFFSET = 32
CELSIUS_MULTIPLIER = 5.0 / 9


def main():
    # Main function to handle user input and display menu
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    return celsius * FAHRENHEIT_MULTIPLIER + FAHRENHEIT_OFFSET


def convert_fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    return CELSIUS_MULTIPLIER * (fahrenheit - FAHRENHEIT_OFFSET)


# Start the program
main()
