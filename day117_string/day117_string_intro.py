""" Day 117: String
Strings are immutable sequences of characters. Most string problems focus on
character frequency, indexing, transformations, and pattern matching.
"""

# Example 1: Reverse a string using two pointers
def example_one():
    """
    Classic two-pointer technique:
    - Convert string to list (mutable)
    - Swap characters from both ends
    - Move pointers inward
    """
    s = list("hello")
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

print("Output Example 1:", example_one())


# Example 2: Check if two strings are anagrams using frequency count
def example_two():
    """
    String frequency pattern:
    - Count characters using dictionary
    - Compare frequency maps
    """
    s = "listen"
    t = "silent"

    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for c in t:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] == 0:
            del freq[c]

    return len(freq) == 0

print("Output Example 2:", example_two())
