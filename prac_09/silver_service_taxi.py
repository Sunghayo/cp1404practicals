"""
CP1404/CP5632 Practical
SilverServiceTaxi class, derived from Taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Fancy Taxi with additional features."""
    flagfall = 4.50  # class variable for flagfall fee

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        fanciness: float, multiplication factor for price per km
        """
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness  # multiply standard price by fanciness

    def get_fare(self):
        """Calculate and return the total fare."""
        # Get fare from parent class and add flagfall
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"