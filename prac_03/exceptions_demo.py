"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- A ValueError will occur if the input for either the numerator or denominator cannot be converted to an integer. This happens if the user enters a non-numeric string
2. When will a ZeroDivisionError occur?
- A ZeroDivisionError will occur if the denominator entered by the user is 0. Dividing by zero is undefined in mathematics, and in Python, it raises this error.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, you can prevent a ZeroDivisionError by checking if the denominator is zero before attempting to divide
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero! Please enter a valid number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")