"""
Estimated Time: 15 minutes
Start Time: 22:00
Actual Time: 22:30
"""

from datetime import datetime


class Guitar:
    """Represent details about a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        name: string, name of the guitar
        year: integer, year the guitar was made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50