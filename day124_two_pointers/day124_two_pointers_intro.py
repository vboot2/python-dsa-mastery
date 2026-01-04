"""Day 124: Two Pointers
Two pointers can be used not only for inward scanning, but also for
pair counting, balancing elements, merging, and minimization checks.
"""


# Example 1: Count pairs with sum less than target
def example_one():
    """
    Sort + two pointers:
    - Fix right pointer
    - Move left pointer up until sum < target
    """
    nums = [3, 1, 5, 2]
    target = 6
    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count


print("Output Example 1:", example_one())


# Example 2: Build minimum average of removed pairs
def example_two():
    """
    Repeatedly remove smallest and largest to compute
    intermediate average sums.
    """
    nums = [4, 2, 9, 5]
    nums.sort()
    averages = []
    left, right = 0, len(nums) - 1

    while left < right:
        avg = (nums[left] + nums[right]) / 2
        averages.append(avg)
        left += 1
        right -= 1

    return averages


print("Output Example 2:", example_two())
