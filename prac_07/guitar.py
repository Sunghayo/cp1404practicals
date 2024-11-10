class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        :param name: string, name of the guitar
        :param year: integer, year the guitar was made
        :param cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars for sorting by year."""
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar calculated from the current year."""
        CURRENT_YEAR = 2024
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is 50 or more years old."""
        return self.get_age() >= 50