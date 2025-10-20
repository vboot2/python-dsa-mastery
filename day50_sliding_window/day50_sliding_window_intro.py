""" 
Day 50: Sliding Window
Sliding Window is an optimization technique that helps reduce time complexity by maintaining a subset of elements (window) that slides across the input, recalculating results efficiently without redundant recomputation.
"""

# Example 1: Fixed-size sliding window (Maximum sum subarray of size k)
def example_one(nums, k):
    # Initialize window sum and max_sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Example 2: Variable-size sliding window (Longest substring without repeating characters)
def example_two(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print("Output Example 1:", example_one([2, 1, 5, 1, 3, 2], 3))
    print("Output Example 2:", example_two("abcabcbb"))
