"""
Day 48: Dynamic Programming (1D, 2D, LCS) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Unique Paths II (LeetCode 63, Medium)
# Link: https://leetcode.com/problems/unique-paths-ii/
# ---------------------------------------------------------
class SolutionUniquePathsII:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0

        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0

        # Fill the grid
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


# ---------------------------------------------------------
# Problem 2: Triangle (LeetCode 120, Medium)
# Link: https://leetcode.com/problems/triangle/
# ---------------------------------------------------------
class SolutionTriangle:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


# ---------------------------------------------------------
# Problem 3: Maximal Square (LeetCode 221, Medium)
# Link: https://leetcode.com/problems/maximal-square/
# ---------------------------------------------------------
class SolutionMaximalSquare:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Unique Paths II:", SolutionUniquePathsII().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print("Triangle Min Path Sum:", SolutionTriangle().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print("Maximal Square Area:", SolutionMaximalSquare().maximalSquare([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]))
