MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

# Constants to replace Magic Numbers
ZERO_COUNT = 0  # Used to replace 0 count check


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = ZERO_COUNT
    number_of_upper = ZERO_COUNT
    number_of_digit = ZERO_COUNT
    number_of_special = ZERO_COUNT

    # TODO: count each kind of character (use str methods like isdigit)
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # TODO: if any of the 'normal' counts are zero, return False
    if number_of_lower == ZERO_COUNT or number_of_upper == ZERO_COUNT or number_of_digit == ZERO_COUNT:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == ZERO_COUNT:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()