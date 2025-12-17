"""
Day 82: DP Sequence/Matrix - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: 1277. Count Square Submatrices with All Ones (Medium)
# Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        total = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    total += dp[i][j]

        return total


# ---------------------------------------------------------
# Problem: 87. Scramble String (Hard)
# Link: https://leetcode.com/problems/scramble-string/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, s1, s2):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                # No swap case
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                # Swap case
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    return True
            return False

        return dfs(s1, s2)


# ---------------------------------------------------------
# Problem: 312. Burst Balloons (Hard)
# Link: https://leetcode.com/problems/burst-balloons/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for length in range(2, n):
            for l in range(n-length):
                r = l + length
                for k in range(l+1, r):
                    dp[l][r] = max(dp[l][r],
                                   nums[l]*nums[k]*nums[r] +
                                   dp[l][k] + dp[k][r])
        return dp[0][n-1]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().solve([[1,1],[1,1]]))

    print("Problem Two Example:",
          SolutionProblemTwo().solve("great", "rgeat"))

    print("Problem Three Example:",
          SolutionProblemThree().solve([3,1,5,8]))
