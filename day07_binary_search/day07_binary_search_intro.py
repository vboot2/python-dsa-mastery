"""
Day 07: Binary Search

Binary Search is a divide-and-conquer algorithm used on sorted arrays.
"""

# Example 1: Basic Binary Search
def binary_search(nums, target):
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

print("Index of 7:", binary_search([1,3,5,7,9,11], 7))


# Example 2: Lower Bound (first index >= target)
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print("Lower bound of 6:", lower_bound([1,3,5,7,9,11], 6))
