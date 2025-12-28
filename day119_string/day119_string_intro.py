""" Day 119: String
String problems often test character properties, case rules, and word-level
transformations using iteration and simple validations.
"""

# Example 1: Detect correct capitalization in a word
def example_one():
    """
    Valid capitalization cases:
    - All letters uppercase
    - All letters lowercase
    - Only first letter uppercase
    """
    word = "Google"

    if word.isupper() or word.islower():
        return True
    return word[0].isupper() and word[1:].islower()

print("Output Example 1:", example_one())


# Example 2: Reverse words in a sentence
def example_two():
    """
    Split sentence by spaces,
    reverse each word individually.
    """
    s = "Let's take LeetCode contest"
    words = s.split(" ")

    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)

print("Output Example 2:", example_two())
