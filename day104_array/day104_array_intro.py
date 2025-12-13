"""
Day 104: Array
Array problems focus on ordering, counting, and sliding window techniques to efficiently
process contiguous or unordered data.
"""

# Example 1: Arrange numbers to form the largest number
def example_one():
    """
    Custom sorting:
    Compare numbers by concatenated order (a+b vs b+a).
    """
    nums = [3, 30, 34, 5, 9]
    nums_str = list(map(str, nums))

    nums_str.sort(key=lambda x: x*10, reverse=True)
    result = "".join(nums_str)

    return result if result[0] != '0' else "0"

print("Output Example 1:", example_one())


# Example 2: Sliding window with frequency counting
def example_two():
    """
    Count subarrays with at most K distinct elements.
    Sliding window expands and shrinks dynamically.
    """
    nums = [1, 2, 1, 2, 3]
    k = 2

    from collections import defaultdict
    freq = defaultdict(int)
    left = 0
    count = 0

    for right in range(len(nums)):
        freq[nums[right]] += 1

        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        count += right - left + 1

    return count

print("Output Example 2:", example_two())
