"""
Day 27: Two Pointers, Greedy, Prefix Sum

These techniques help optimize problems by reducing brute force complexity.
- Two Pointers: Move pointers inward/outward to optimize traversals.
- Greedy: Make the locally optimal choice step by step.
- Prefix Sum: Store cumulative sums to quickly compute subarray sums.
"""

# Example 1: Two Pointers - Pair Sum Check
def example_one(nums, target):
    # 🔹 Assumes nums is sorted
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False

print("Output Example 1:", example_one([1, 2, 4, 7, 11], 15))  # True

# Example 2: Prefix Sum - Subarray Sum in O(1)
def example_two(nums, i, j):
    # 🔹 Precompute prefix sums
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    # sum of nums[i:j+1] = prefix[j+1] - prefix[i]
    return prefix[j+1] - prefix[i]

print("Output Example 2:", example_two([2, 4, 6, 8, 10], 1, 3))  # 18
