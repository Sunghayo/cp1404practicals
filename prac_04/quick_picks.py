import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate random quick picks based on user input."""
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate a list of unique random numbers in sorted order."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()  # Sort the numbers in ascending order
    return quick_pick


def print_quick_pick(quick_pick):
    """Print the quick pick numbers"""
    for number in quick_pick:
        print(f"{number:2}", end=" ")
    print()


main()
