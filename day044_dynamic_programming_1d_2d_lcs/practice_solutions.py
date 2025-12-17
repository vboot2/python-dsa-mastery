"""
Day 44: Dynamic Programming (1D, 2D, LCS) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: House Robber II (LeetCode 213, Medium)
# Link: https://leetcode.com/problems/house-robber-ii/
# ---------------------------------------------------------
class SolutionHouseRobberII:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(arr):
            prev, curr = 0, 0
            for n in arr:
                prev, curr = curr, max(curr, prev + n)
            return curr
        
        # Rob houses excluding first OR excluding last (circular arrangement)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ---------------------------------------------------------
# Problem 2: Longest Increasing Subsequence (LeetCode 300, Medium)
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# ---------------------------------------------------------
class SolutionLIS:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# ---------------------------------------------------------
# Problem 3: Longest Common Subsequence (LeetCode 1143, Medium)
# Link: https://leetcode.com/problems/longest-common-subsequence/
# ---------------------------------------------------------
class SolutionLCS:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("House Robber II Example:", SolutionHouseRobberII().rob([2,3,2]))
    print("LIS Example:", SolutionLIS().lengthOfLIS([10,9,2,5,3,7,101,18]))
    print("LCS Example:", SolutionLCS().longestCommonSubsequence("abcde", "ace"))
