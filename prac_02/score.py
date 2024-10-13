import random
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def main():
    # Main function to get score input and print result
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score}\n{random_result}")


def evaluate_score(score):
    # Evaluate the given score and return the result string
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


# Start the program
main()
