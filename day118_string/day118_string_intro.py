""" Day 118: String
String problems often involve counting, parsing, formatting, and pattern detection
using hash maps, iteration, and mathematical observations.
"""

# Example 1: Longest Palindrome length from a string
def example_one():
    """
    Key idea:
    - Count character frequencies
    - Use all even counts
    - Use at most one odd count in the center
    """
    from collections import Counter

    s = "abccccdd"
    freq = Counter(s)
    length = 0
    odd_found = False

    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    return length + (1 if odd_found else 0)

print("Output Example 1:", example_one())


# Example 2: Check if string is built by repeating a substring
def example_two():
    """
    Trick:
    - If s is a repeated substring pattern,
      it will exist inside (s + s)[1:-1]
    """
    s = "abab"
    return s in (s + s)[1:-1]

print("Output Example 2:", example_two())
