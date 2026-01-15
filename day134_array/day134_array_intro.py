"""Day 134: Array
This lesson focuses on array construction, in-place rotations,
stack-based evaluation, and grid boundary processing.
"""


# Example 1: Rotate array to the right by k steps
def example_one():
    """
    Reverse technique:
    - Reverse whole array
    - Reverse first k
    - Reverse remaining
    """
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    k %= len(nums)

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums


print("Output Example 1:", example_one())


# Example 2: Build target array with insert operations
def example_two():
    """
    Insert nums[i] at index[i].
    """
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    target = []

    for n, i in zip(nums, index):
        target.insert(i, n)

    return target


print("Output Example 2:", example_two())
