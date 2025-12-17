"""
Day 73: Monotonic Stack
"""

# -----------------------------------------------
# Example 1: Next Greater Element using Monotonic Stack
# -----------------------------------------------


def example_one(nums):
    """
    For each element, find the next greater number to its right.
    Uses a decreasing monotonic stack.
    """
    stack = []  # store indices
    res = [-1] * len(nums)
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        stack.append(i)
    return res


print("Output Example 1:", example_one([2, 1, 2, 4, 3]))  # Expected: [4, 2, 4, -1, -1]


# -----------------------------------------------
# Example 2: Previous Smaller Element (variant)
# -----------------------------------------------


def example_two(nums):
    """
    Finds the previous smaller element for each position.
    Uses an increasing monotonic stack.
    """
    stack = []
    res = [-1] * len(nums)
    for i, n in enumerate(nums):
        while stack and stack[-1] >= n:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(n)
    return res


print(
    "Output Example 2:", example_two([2, 5, 1, 4, 8, 3, 2])
)  # Expected: [-1, 2, -1, 1, 4, 1, 1]
