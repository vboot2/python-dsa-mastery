"""
Day 04: Two Pointers
"""

# Example 1: Opposite ends
nums = [1, 2, 3, 4, 5]
left, right = 0, len(nums) - 1
while left < right:
    print(f"Checking pair: {nums[left]}, {nums[right]}")
    left += 1
    right -= 1

# Example 2: Fast & slow pointers
nums = [1, 2, 3, 4, 5]
slow, fast = 0, 0
while fast < len(nums) and fast + 1 < len(nums):
    slow += 1
    fast += 2
    print(f"Slow at {slow}, Fast at {fast}")
