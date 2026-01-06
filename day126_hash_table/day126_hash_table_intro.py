"""Day 126: Hash Table
Hash tables excel at counting, grouping, and fast membership checks,
making them ideal for frequency-based and mapping problems.
"""


# Example 1: Check if all elements can be grouped equally
def example_one():
    """
    Use a frequency map:
    - Count occurrences
    - Check if all counts share a common divisor > 1
    """
    from collections import Counter
    import math

    deck = [1, 1, 2, 2, 2, 2]
    freq = Counter(deck)

    gcd_val = 0
    for count in freq.values():
        gcd_val = math.gcd(gcd_val, count)

    return gcd_val >= 2


print("Output Example 1:", example_one())


# Example 2: Count characters using hash table
def example_two():
    """
    Count letters in a word using dictionary.
    """
    word = "balloon"
    freq = {}

    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


print("Output Example 2:", example_two())
