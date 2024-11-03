"""
Estimated Time: 15 minutes
Start Time: 22:30
Actual Time: 22:45

A class representing a Programming Language with specific attributes.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize a ProgrammingLanguage instance.

        name: string, name of the language
        typing: string, static or dynamic
        reflection: boolean, whether language supports reflection
        year: integer, year language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language is dynamically typed, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
