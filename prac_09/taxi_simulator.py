"""
CP1404/CP5632 Practical
Taxi Simulator Program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    total_bill = 0
    current_taxi = None
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    print("Let's drive!")
    print_menu()
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def print_menu():
    """Display menu for user input."""
    print("q)uit, c)hoose taxi, d)rive")


def choose_taxi(taxis):
    """Display available taxis and get user's choice."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(current_taxi, bill):
    """Drive the chosen taxi and return updated bill."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill

    try:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        current_taxi.start_fare()
        return bill + fare
    except ValueError:
        print("Invalid distance")
        return bill


def display_taxis(taxis):
    """Display all taxis with their details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()