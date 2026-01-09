"""Day 127: Array
Array problems focus on traversal, prefix calculations,
simulation, and maintaining invariants over contiguous elements.
"""


# Example 1: Find pivot index in an array
def example_one():
    """
    Prefix sum approach:
    - Total sum known
    - Track left sum while iterating
    """
    nums = [1, 7, 3, 6, 5, 6]
    total = sum(nums)
    left_sum = 0

    for i, n in enumerate(nums):
        if left_sum == total - left_sum - n:
            return i
        left_sum += n

    return -1


print("Output Example 1:", example_one())


# Example 2: Check if array is monotonic
def example_two():
    """
    Track increasing and decreasing flags.
    """
    nums = [1, 2, 2, 3]
    inc = dec = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            inc = False
        if nums[i] > nums[i - 1]:
            dec = False

    return inc or dec


print("Output Example 2:", example_two())
