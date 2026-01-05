"""Day 125: Hash Table
Hash tables allow fast lookups, counting, and membership checks,
typically achieving O(1) average time complexity.
"""


# Example 1: Frequency counting using hash table
def example_one():
    """
    Count frequency of characters in a string
    using a dictionary (hash table).
    """
    s = "leetcode"
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


print("Output Example 1:", example_one())


# Example 2: Find first unique character
def example_two():
    """
    Two-pass hash table approach:
    - First pass: count frequencies
    - Second pass: find first char with count == 1
    """
    s = "loveleetcode"
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


print("Output Example 2:", example_two())
