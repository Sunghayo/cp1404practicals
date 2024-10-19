"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""

def main():
    """Store emails and extract names from them."""
    email = input("Email: ")

    while email != "":
        name = extract_name_from_email(email)
        print(f"Extracted name: {name}")
        email = input("Email: ")


def extract_name_from_email(email):
    """Extract the user's name from their email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()  # Capitalizes the first letter of each word
    return name


main()