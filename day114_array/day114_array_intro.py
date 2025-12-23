""" Day 114: Array
Array problems often rely on indexing tricks, in-place marking, and linear scans
to achieve optimal time and space complexity.
"""

# Example 1: Find missing numbers using in-place marking
def example_one():
    """
    Mark visited indices by negating values.
    """
    nums = [4,3,2,7,8,2,3,1]

    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)

    return missing


print("Output Example 1:", example_one())


# Example 2: Count maximum consecutive ones
def example_two():
    """
    Sliding window / running count.
    """
    nums = [1,1,0,1,1,1]
    max_count = count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


print("Output Example 2:", example_two())
