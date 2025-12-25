""" Day 116: String
String problems focus on parsing, comparison, pattern matching,
and mapping characters to values using simple rules or hash maps.
"""

# Example 1: Roman numeral to integer conversion
def example_one():
    """
    Traverse string left to right.
    If current value < next value, subtract; else add.
    """
    roman = {"I": 1, "V": 5, "X": 10}
    s = "IX"
    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total


print("Output Example 1:", example_one())


# Example 2: Check isomorphic strings
def example_two():
    """
    Maintain two-way mapping between characters.
    """
    s = "egg"
    t = "add"

    map_st = {}
    map_ts = {}

    for a, b in zip(s, t):
        if a in map_st and map_st[a] != b:
            return False
        if b in map_ts and map_ts[b] != a:
            return False
        map_st[a] = b
        map_ts[b] = a

    return True


print("Output Example 2:", example_two())
