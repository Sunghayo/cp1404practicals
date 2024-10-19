"""
Word Occurrences
Estimate: 25 minutes
Actual:
"""

def main():
    """Main function to read the Wimbledon data and process the results."""
    filename = "wimbledon.csv"
    records = read_wimbledon_data(filename)
    champion_wins = count_champion_wins(records)
    countries = extract_countries(records)
    # The display function will be implemented in the next step


def read_wimbledon_data(filename):
    """Read Wimbledon data from a file and return a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            record = line.strip().split(",")
            records.append(record)
    return records


def count_champion_wins(records):
    """Count how many times each champion has won and return a dictionary."""
    champion_wins = {}
    for record in records:
        champion = record[2]
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    return champion_wins


def extract_countries(records):
    """Extract the countries of the champions and return a set of unique countries."""
    countries = {record[1] for record in records}  # Using a set for unique countries
    return countries


main()