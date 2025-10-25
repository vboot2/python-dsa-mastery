"""
Day 55: Merge Intervals
Understanding merging patterns through sorted ranges, counting logic, and 2D interval geometry.
"""


# Example 1: Merge consecutive integer ranges into compact summaries
def example_one(nums):
    """
    Demonstrates how to combine consecutive numbers into summary ranges.
    Example: [0,1,2,4,5,7] -> ["0->2", "4->5", "7"]
    """
    if not nums:
        return []

    res = []
    start = nums[0]
    for i in range(1, len(nums)):
        # If gap detected, record previous range
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i - 1]}")
            start = nums[i]
    # Append last range
    if start == nums[-1]:
        res.append(str(start))
    else:
        res.append(f"{start}->{nums[-1]}")
    return res


# Example 2: Count positive and negative intervals in sorted array
def example_two(nums):
    """
    Counts how many positive and negative numbers exist in sorted array.
    Conceptually, this partitions number line into two intervals.
    """
    pos = sum(1 for x in nums if x > 0)
    neg = sum(1 for x in nums if x < 0)
    return max(pos, neg)


print("Output Example 1:", example_one([0, 1, 2, 4, 5, 7]))
print("Output Example 2:", example_two([-5, -3, -1, 0, 2, 3, 4]))
