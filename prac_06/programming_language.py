"""
Estimated Time: 15 minutes
Start Time: 15
Actual Time:

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