"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function to load data and display subject details."""
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the newline character
            parts = line.split(',')  # Split the line into its parts
            parts[2] = int(parts[2])  # Convert the student number to an integer
            data.append(parts)  # Append the list of parts (subject, lecturer, number)
    return data


def display_subject_details(subjects):
    """Display formatted details about subjects, lecturers, and student numbers."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()

