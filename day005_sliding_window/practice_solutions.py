"""
Day 05: Sliding Window - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Maximum Average Subarray I (LeetCode 643, Easy)
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# ---------------------------------------------------------
class SolutionMaxAverageSubarray:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k


# ---------------------------------------------------------
# Problem: Longest Substring Without Repeating Characters (LeetCode 3, Medium)
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# ---------------------------------------------------------
class SolutionLongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


# ---------------------------------------------------------
# Problem: Minimum Size Subarray Sum (LeetCode 209, Medium)
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# ---------------------------------------------------------
class SolutionMinSubarrayLen:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Maximum Average Subarray I Example 1:", 
          SolutionMaxAverageSubarray().findMaxAverage([1,12,-5,-6,50,3], 4))
    print("Maximum Average Subarray I Example 2:", 
          SolutionMaxAverageSubarray().findMaxAverage([5], 1))
    
    print("Longest Substring Without Repeating Characters Example 1:", 
          SolutionLongestSubstring().lengthOfLongestSubstring("abcabcbb"))
    print("Longest Substring Without Repeating Characters Example 2:", 
          SolutionLongestSubstring().lengthOfLongestSubstring("bbbbb"))
    print("Longest Substring Without Repeating Characters Example 3:", 
          SolutionLongestSubstring().lengthOfLongestSubstring("pwwkew"))
    
    print("Minimum Size Subarray Sum Example 1:", 
          SolutionMinSubarrayLen().minSubArrayLen(7, [2,3,1,2,4,3]))
    print("Minimum Size Subarray Sum Example 2:", 
          SolutionMinSubarrayLen().minSubArrayLen(4, [1,4,4]))
    print("Minimum Size Subarray Sum Example 3:", 
          SolutionMinSubarrayLen().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
