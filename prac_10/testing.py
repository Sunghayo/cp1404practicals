"""
CP1404/CP5632 Practical
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter
    and ending with a single period.
    >>> format_phrase("hello")
    'Hello.'
    >>> format_phrase("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase("this is a test")
    'This is a test.'
    """
    phrase = phrase.strip()
    if not phrase.endswith("."):
        phrase += "."
    return phrase.capitalize()


def run_tests():
    """Run the tests on the functions."""
    # Assert test for repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Assert tests for Car class
    car = Car()
    assert car.fuel == 0, "Car default fuel should be 0"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car should set fuel to 10 when initialized with fuel=10"

    # Uncomment this line to run doctests
    doctest.testmod()


if __name__ == '__main__':
    run_tests()