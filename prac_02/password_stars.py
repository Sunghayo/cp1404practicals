MIN_PASSWORD_LENGTH = 6


def main():
    # Get valid password from the user
    password = get_password()
    # Print the asterisks from the password length
    print_asterisks(password)


def get_password():
    # Prompts the user for a password and checks its length
    password = input("Enter your password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password is too short! It must be at least {MIN_PASSWORD_LENGTH} characters long.")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    # Prints asterisks from the length of the password
    print('*' * len(password))


# Start program
main()
