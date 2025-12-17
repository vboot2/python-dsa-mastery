"""
Day 25: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem: Sum of All Odd Length Subarrays (LeetCode 1588, Easy)
# Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# ---------------------------------------------------------
class SolutionOddLengthSubarrays:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        total = 0
        for i in range(n):
            for j in range(i, n, 2):  # only odd lengths
                total += prefix[j+1] - prefix[i]
        return total


# ---------------------------------------------------------
# Problem: Product of Array Except Self (LeetCode 238, Medium)
# Link: https://leetcode.com/problems/product-of-array-except-self/
# ---------------------------------------------------------
class SolutionProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 1588 Example:", SolutionOddLengthSubarrays().sumOddLengthSubarrays([1,4,2,5,3]))
    print("Problem 238 Example:", SolutionProductExceptSelf().productExceptSelf([1,2,3,4]))
