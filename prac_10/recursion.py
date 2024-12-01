"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
"""
n = 5 → 5 % 2 = 1
n = 4 → 4 % 2 = 0
n = 3 → 3 % 2 = 1
n = 2 → 2 % 2 = 0
n = 1 → 1 % 2 = 1
n = 0 → base case, return 0
1 + 0 + 1 + 0 + 1 = 3
"""

# TODO: 2. use the debugger to step through and see what's actually happening
#do_it(5) → [5, 3, 1] → 3
#do_it(6) → [5, 3, 1] → 3
#do_it(10) → [9, 7, 5, 3, 1] → 5


print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# The function lacks a proper base case to stop recursion, so it will result in infinite recursion and eventually cause a RecursionError.
# The condition if n < 0 is checked, but it doesn’t stop the recursion or print squares correctly.

# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)
# The function continuously decrements n without a stopping condition.
# When n becomes negative, the condition if n < 0: is true, but it attempts to compute n ** 2 for negative values unnecessarily.
# This creates infinite recursion, leading to a runtime error.

# TODO: 5. fix do_something() so that it works according to the docstring
def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return  # Base case: Stop recursion when n is negative
    print(n ** 2)  # Print the square of the current number
    do_something(n - 1)  # Recursive call with n decremented
