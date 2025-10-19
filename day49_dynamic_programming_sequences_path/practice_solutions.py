"""
Day 49: Dynamic Programming (Sequences & Path Minimization) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Largest Divisible Subset (LeetCode 368, Medium)
# Link: https://leetcode.com/problems/largest-divisible-subset/
# ---------------------------------------------------------
class SolutionLargestDivisibleSubset:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n           # length of largest subset ending at i
        parent = [-1] * n      # parent pointers to rebuild subset
        max_len, max_idx = 1, 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len, max_idx = dp[i], i

        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
        return res[::-1]


# ---------------------------------------------------------
# Problem 2: Wiggle Subsequence (LeetCode 376, Medium)
# Link: https://leetcode.com/problems/wiggle-subsequence/
# ---------------------------------------------------------
class SolutionWiggleSubsequence:
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)


# ---------------------------------------------------------
# Problem 3: Minimum Falling Path Sum (LeetCode 931, Medium)
# Link: https://leetcode.com/problems/minimum-falling-path-sum/
# ---------------------------------------------------------
class SolutionMinFallingPathSum:
    def minFallingPathSum(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        # bottom-up DP modifying matrix in-place
        for i in range(n-2, -1, -1):
            for j in range(n):
                best = matrix[i+1][j]
                if j > 0:
                    best = min(best, matrix[i+1][j-1])
                if j < n-1:
                    best = min(best, matrix[i+1][j+1])
                matrix[i][j] += best
        return min(matrix[0])


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Largest Divisible Subset:", SolutionLargestDivisibleSubset().largestDivisibleSubset([1,2,4,8]))
    print("Wiggle Subsequence Length:", SolutionWiggleSubsequence().wiggleMaxLength([1,7,4,9,2,5]))
    print("Min Falling Path Sum:", SolutionMinFallingPathSum().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
