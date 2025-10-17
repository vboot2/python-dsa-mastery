"""
Day 47: Dynamic Programming (Grid Paths) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Unique Paths (LeetCode 62, Medium)
# Link: https://leetcode.com/problems/unique-paths/
# ---------------------------------------------------------
class SolutionUniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# ---------------------------------------------------------
# Problem 2: Minimum Path Sum (LeetCode 64, Medium)
# Link: https://leetcode.com/problems/minimum-path-sum/
# ---------------------------------------------------------
class SolutionMinPathSum:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Fill first row and column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]


# ---------------------------------------------------------
# Problem 3: Interleaving String (LeetCode 97, Medium)
# Link: https://leetcode.com/problems/interleaving-string/
# ---------------------------------------------------------
class SolutionInterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Unique Paths:", SolutionUniquePaths().uniquePaths(3, 7))
    print("Min Path Sum:", SolutionMinPathSum().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print("Interleaving String:", SolutionInterleavingString().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
