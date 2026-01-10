"""Day 130: Array
Array problems here focus on geometry counting, monotonic checks,
simulation, and basic greedy logic.
"""


# Example 1: Check if an array is monotonic
def example_one():
    """
    An array is monotonic if it is entirely non-increasing
    or non-decreasing.
    """
    nums = [1, 2, 2, 3]
    inc = dec = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            inc = False
        if nums[i] > nums[i - 1]:
            dec = False

    return inc or dec


print("Output Example 1:", example_one())


# Example 2: Add integer to array-form number
def example_two():
    """
    Simulate digit-by-digit addition from the end.
    """
    num = [9, 9, 9]
    k = 1
    i = len(num) - 1

    while i >= 0 or k > 0:
        if i >= 0:
            k += num[i]
            num[i] = k % 10
            k //= 10
            i -= 1
        else:
            num.insert(0, k % 10)
            k //= 10

    return num


print("Output Example 2:", example_two())
