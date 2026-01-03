"""Day 123: Two Pointers
Two pointers can be extended to handle comparisons across arrays, adjacent
elements, prefix/suffix building, and greedy matching.
"""


# Example 1: Count arithmetic triplets using two pointers
def example_one():
    """
    Given a sorted list, use two pointers to find triplets
    where nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.
    """
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    n = len(nums)
    count = 0

    i = 0
    for j in range(n):
        while nums[j] - nums[i] > diff:
            i += 1
        if nums[j] - nums[i] == diff and (nums[j] + diff) in nums:
            count += 1

    return count


print("Output Example 1:", example_one())


# Example 2: Find largest positive number with its negative present
def example_two():
    """
    Use two pointers on a sorted array:
    - Left from smallest (negative)
    - Right from largest (positive)
    """
    nums = [-1, 2, -3, 3]
    nums.sort()
    left, right = 0, len(nums) - 1
    result = -1

    while left < right:
        if abs(nums[left]) == nums[right]:
            result = nums[right]
            left += 1
            right -= 1
        elif abs(nums[left]) > nums[right]:
            left += 1
        else:
            right -= 1

    return result


print("Output Example 2:", example_two())
