"""
Day 102: Greedy / String
Greedy + String problems require making optimal local decisions while parsing or modifying string data structures.
"""

# Example 1: Greedy assignment — assign cookies to children
def example_one():
    """
    Classic greedy rule:
    - Sort children by greed
    - Sort cookies by size
    - Try to satisfy the smallest greed first
    """
    greed = [1, 2, 3]
    cookies = [1, 1]

    greed.sort()
    cookies.sort()

    i = j = 0
    satisfied = 0

    while i < len(greed) and j < len(cookies):
        if cookies[j] >= greed[i]:
            satisfied += 1
            i += 1
            j += 1
        else:
            j += 1

    return satisfied

print("Output Example 1:", example_one())


# Example 2: String validation using greedy rules
def example_two():
    """
    Check if a string represents a valid number (simple variant):
    - Must contain digits
    - Optional leading +/- sign
    - At most one dot
    """
    s = "+12.45"
    digits = 0
    dot = 0
    i = 0

    if s and (s[0] == '+' or s[0] == '-'):
        i += 1

    while i < len(s):
        if s[i].isdigit():
            digits += 1
        elif s[i] == '.':
            dot += 1
            if dot > 1:
                return False
        else:
            return False
        i += 1

    return digits > 0

print("Output Example 2:", example_two())
