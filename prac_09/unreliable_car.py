"""
CP1404/CP5632 Practical
UnreliableCar class, derived from Car
"""
from unreliable_car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of Car that may not drive."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float between 0 and 100, chance that the car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only if it is reliable enough.

        Returns the distance driven, which will be 0 if the car is unreliable.
        """
        random_chance = randint(0, 100)
        if random_chance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven