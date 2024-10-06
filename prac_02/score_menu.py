MIN_SCORE = 0
MAX_SCORE = 100


def main():
    # Main function to display menu and handle user choices
    score = get_valid_score()
    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice.")
        display_menu()
        choice = input(">>> ").upper()

    print("Farewell")


def display_menu():
    # Display the menu options
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    # Get a valid score between 0 and 100 inclusive
    score = int(input("Enter a score (0-100): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print(f"Invalid score. Please enter a score between {MIN_SCORE} and {MAX_SCORE}.")
        score = int(input("Enter a score (0-100): "))
    return score


def determine_result(score):
    # Determine the result based on the score
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    # Print as many stars as the score
    print('*' * score)


# Start the program
main()