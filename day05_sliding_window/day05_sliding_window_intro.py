"""
Day 05: Sliding Window

The sliding window technique allows solving subarray/substring problems
efficiently by maintaining a "window" and adjusting it as we move.
"""

# Example 1: Fixed window sum (subarray of size 3)
nums = [1, 2, 3, 4, 5]
k = 3
window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i-k]
    max_sum = max(max_sum, window_sum)

print("Max sum of subarray of size 3:", max_sum)

# Example 2: Variable window
s = "abcabcbb"
seen = set()
left = 0
max_len = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print("Longest substring without repeating chars:", max_len)
