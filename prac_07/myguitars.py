from guitar import Guitar


def load_guitars(filename="guitars.csv"):
    """Load guitars from the CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and split the line into parts
            parts = line.strip().split(',')
            # Create Guitar object and append to list
            # Note: we need to convert year to int and cost to float
            name = parts[0].strip()
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars, header=""):
    """Display the guitars with optional header."""
    if header:
        print(header)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def get_new_guitar():
    """Get guitar details from user input."""
    print("Enter your new guitar details:")
    name = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            return Guitar(name, year, cost)
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


def save_guitars(guitars, filename="guitars.csv"):
    """Save the guitars to the CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    """Main program for guitar management."""
    print("My Guitars!")
    guitars = load_guitars()

    # Display the original list
    display_guitars(guitars, "\nThese are my guitars:")

    # Sort and display by year
    guitars.sort()  # This will use the __lt__ method we defined
    display_guitars(guitars, "\nGuitars sorted by year:")

    # Add new guitars
    while True:
        choice = input("\nDo you want to add a new guitar? (Y/n) ").lower()
        if choice in ['', 'y']:
            new_guitar = get_new_guitar()
            guitars.append(new_guitar)
            print(f"{new_guitar.name} has been added.")
        else:
            break

    # Save all guitars back to file
    save_guitars(guitars)
    print("\nGuitars have been saved to guitars.csv")


if __name__ == '__main__':
    main()