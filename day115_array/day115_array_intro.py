""" Day 115: Array
Array problems often involve sorting, reshaping, counting frequencies,
and greedy pairing to achieve optimal results.
"""

# Example 1: Greedy pairing after sorting
def example_one():
    """
    Pair smallest numbers together to maximize sum of minimums.
    """
    nums = [1, 4, 3, 2]
    nums.sort()

    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]

    return total


print("Output Example 1:", example_one())


# Example 2: Frequency counting using dictionary
def example_two():
    """
    Count elements and find the longest harmonious subsequence.
    """
    nums = [1,3,2,2,5,2,3,7]
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    longest = 0
    for k in freq:
        if k + 1 in freq:
            longest = max(longest, freq[k] + freq[k + 1])

    return longest


print("Output Example 2:", example_two())
