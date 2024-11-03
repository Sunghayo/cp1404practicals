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