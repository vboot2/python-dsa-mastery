"""
Day 103: String / Array
String and array manipulation often involve parsing, two-pointer techniques, and careful handling
of edge cases while transforming sequences.
"""

# Example 1: Reverse words in a string
def example_one():
    """
    Split → reverse list → join.
    Demonstrates typical string processing flow.
    """
    s = "hello world this is dsa"
    words = s.split()
    words.reverse()
    return " ".join(words)

print("Output Example 1:", example_one())


# Example 2: Two-pointer technique on arrays
def example_two():
    """
    Remove duplicates from a sorted array using two pointers.
    """
    nums = [1, 1, 2, 2, 3, 4, 4]
    w = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[w] = nums[r]
            w += 1

    return nums[:w]

print("Output Example 2:", example_two())
