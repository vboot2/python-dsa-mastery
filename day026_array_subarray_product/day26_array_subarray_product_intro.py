"""
Day 26: Array, Subarray, and Product Problems

- Shortest Unsorted Continuous Subarray (Greedy, Sorting insight)
- Maximum Product Subarray (Dynamic Programming with running max/min)
"""

# Example 1: Detect unsorted subarray
def example_one():
    nums = [2,6,4,8,10,9,15]
    sorted_nums = sorted(nums)
    left, right = 0, len(nums)-1
    while left < len(nums) and nums[left] == sorted_nums[left]:
        left += 1
    while right > left and nums[right] == sorted_nums[right]:
        right -= 1
    return right - left + 1

print("Output Example 1 (Unsorted subarray length):", example_one())


# Example 2: Maximum product subarray
def example_two():
    nums = [2,3,-2,4]
    max_prod = min_prod = result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)
    return result

print("Output Example 2 (Maximum product subarray):", example_two())
