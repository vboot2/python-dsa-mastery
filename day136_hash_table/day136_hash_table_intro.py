"""Day 136: Hash Table
Hash tables provide O(1) average-time lookup and are ideal for
frequency counting, fast membership checks, and state tracking.
"""


# Example 1: Check if a path crosses itself
def example_one():
    """
    Use a set to store visited coordinates.
    If a coordinate is visited again → path crosses.
    """
    path = "NESWW"
    x = y = 0
    visited = {(0, 0)}

    for move in path:
        if move == "N":
            y += 1
        elif move == "S":
            y -= 1
        elif move == "E":
            x += 1
        else:
            x -= 1

        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False


print("Output Example 1:", example_one())


# Example 2: Count character frequency
def example_two():
    """
    Classic frequency map using dictionary.
    """
    s = "leetcode"
    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    return freq


print("Output Example 2:", example_two())
