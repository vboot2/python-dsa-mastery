""" Day 112: Array
Arrays store elements in contiguous memory, allowing O(1) access and efficient iteration for many problems.
"""

# Example 1: Remove duplicates from a sorted array (in-place idea)
def example_one():
    """
    Two-pointer technique:
    - One pointer tracks position of unique elements
    - Other pointer scans the array
    """
    nums = [1, 1, 2, 2, 3]
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i + 1]


print("Output Example 1:", example_one())


# Example 2: Find element with maximum frequency
def example_two():
    """
    Boyer-Moore style idea:
    Count balance of elements.
    """
    nums = [2, 2, 1, 1, 2, 2]
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


print("Output Example 2:", example_two())
