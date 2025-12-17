"""
Day 26: Array, Subarray, and Product Problems - LeetCode Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem: Shortest Unsorted Continuous Subarray (LeetCode 581, Medium)
# Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# ---------------------------------------------------------
class SolutionShortestUnsortedSubarray:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums)-1
        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1
        while right > left and nums[right] == sorted_nums[right]:
            right -= 1
        return right - left + 1 if right > left else 0


# ---------------------------------------------------------
# Problem: Maximum Product Subarray (LeetCode 152, Medium)
# Link: https://leetcode.com/problems/maximum-product-subarray/
# ---------------------------------------------------------
class SolutionMaxProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            result = max(result, max_prod)
        return result


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 581 Example:", SolutionShortestUnsortedSubarray().findUnsortedSubarray([2,6,4,8,10,9,15]))
    print("Problem 152 Example:", SolutionMaxProductSubarray().maxProduct([2,3,-2,4]))
