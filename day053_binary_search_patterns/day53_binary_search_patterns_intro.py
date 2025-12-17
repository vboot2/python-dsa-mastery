"""
Day 53: Binary Search Patterns
Binary Search divides the search space in half at each step to efficiently locate a target or satisfy a condition in O(log n) time.
"""


# Example 1: Basic binary search in a sorted array
def example_one(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example 2: Finding the smallest element greater than or equal to target (lower bound)
def example_two(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(nums) else -1


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print("Output Example 1:", example_one(nums, 7))  # Expected: 3
    print("Output Example 2:", example_two(nums, 8))  # Expected: 4
