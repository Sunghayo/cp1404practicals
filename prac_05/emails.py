"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""

def main():
    """Store emails and allow users to confirm or input their names."""
    email = input("Email: ")

    while email != "":
        name = extract_name_from_email(email)
        is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_name_correct != "" and is_name_correct != 'y':
            name = input("Name: ")

        print(f"Stored: {name} ({email})")
        email = input("Email: ")


def extract_name_from_email(email):
    """Extract the user's name from their email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()  # Capitalizes the first letter of each word
    return name


main()

