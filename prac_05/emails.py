"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""

def main():
    """Store emails and names in a dictionary and print them."""
    emails_to_names = {}
    email = input("Email: ")

    while email != "":
        name = extract_name_from_email(email)
        is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_name_correct != "" and is_name_correct != 'y':
            name = input("Name: ")

        emails_to_names[email] = name  # Store email and name in the dictionary
        email = input("Email: ")

    print("\nStored email and names:")
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract the user's name from their email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()  # Capitalizes the first letter of each word
    return name


main()

