"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

def main():
    """Count occurrences of words in a user-provided text."""
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    display_word_occurrences(word_counts)


def count_word_occurrences(text):
    """Count occurrences of each word in the text."""
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def display_word_occurrences(word_counts):
    """Display word occurrences sorted and aligned."""
    words = list(word_counts.keys())
    words.sort()

    max_length = max(len(word) for word in words)
    for word in words:
        print(f"{word:{max_length}} : {word_counts[word]}")


main()
