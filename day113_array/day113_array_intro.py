""" Day 113: Array
Arrays allow efficient traversal and in-place manipulation, often solved using hashing or two-pointer techniques.
"""

# Example 1: Move all zeros to the end (order preserved)
def example_one():
    """
    Two-pointer approach:
    - One pointer tracks position of next non-zero
    - Another scans the array
    """
    nums = [0, 1, 0, 3, 12]
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return nums


print("Output Example 1:", example_one())


# Example 2: Find intersection of two arrays using sets
def example_two():
    """
    Use set intersection for uniqueness.
    """
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    return list(set(nums1) & set(nums2))


print("Output Example 2:", example_two())
