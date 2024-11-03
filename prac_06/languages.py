"""
Estimated Time: 10 minutes
Start Time: 22:50
Actual Time: 23:00

Client code to test ProgrammingLanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    # Create programming language objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)


main()