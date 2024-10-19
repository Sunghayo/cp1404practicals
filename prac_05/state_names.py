"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}


def main():
    """Main program to handle state code input and print state names."""
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase to handle lowercase entries
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    print("\nAll states:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code:3} is {name}")


main()
