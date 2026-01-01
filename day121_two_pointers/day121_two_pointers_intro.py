""" Day 121: Two Pointers
Two pointers use indices moving from different directions or speeds to efficiently
process arrays or strings without extra space.
"""

# Example 1: Reverse only letters in a string
def example_one():
    """
    Two pointers from both ends:
    - Skip non-letter characters
    - Swap letters and move inward
    """
    s = list("a-bC-dEf-ghIj")
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

print("Output Example 1:", example_one())


# Example 2: Check if long pressed name is valid
def example_two():
    """
    Two pointers:
    - Pointer i on name
    - Pointer j on typed
    Allow repeated characters in typed
    """
    name = "alex"
    typed = "aaleex"

    i = j = 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False

    return i == len(name)

print("Output Example 2:", example_two())
