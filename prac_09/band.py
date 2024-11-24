"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class that contains musicians using aggregation."""

    def __init__(self, name=""):
        """Construct a Band object.

        Args:
            name (str): name of the band (defaults to empty string)
        """
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band with its musicians.

        Returns:
            str: string in format 'band_name (musician1, musician2, ...)'
        """
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band.

        Args:
            musician (Musician): a musician object to be added to the band
        """
        self.musicians.append(musician)

    def play(self):
        """Return a string showing all musicians playing their instruments.

        Returns:
            str: Multi-line string with each musician playing or needing an instrument
        """
        return '\n'.join(musician.play() for musician in self.musicians)