"""Day 127: Hash Table
Hash tables are useful for frequency analysis, mapping ranks,
detecting patterns, and grouping values efficiently.
"""


# Example 1: Check if all frequencies are unique
def example_one():
    """
    Use a hash table to count frequencies,
    then store frequencies in a set.
    """
    nums = [1, 2, 2, 1, 1, 3]
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    return len(freq.values()) == len(set(freq.values()))


print("Output Example 1:", example_one())


# Example 2: Rank transform of an array
def example_two():
    """
    Map each unique value to its rank after sorting.
    """
    arr = [40, 10, 20, 30]
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}

    return [rank[x] for x in arr]


print("Output Example 2:", example_two())
