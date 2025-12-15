"""
Day 106: DP/Graph - LeetCode Problem Solutions
"""

from typing import List
from collections import deque


# ---------------------------------------------------------
# Problem: Palindrome Partitioning III (LeetCode 1278, Hard)
# Link: https://leetcode.com/problems/palindrome-partitioning-iii/
# ---------------------------------------------------------
class SolutionProblemOne:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        DP:
        - cost[i][j]: changes to make s[i:j+1] a palindrome
        - dp[i][p]: min changes to split s[:i] into p palindromes
        """
        n = len(s)

        # compute palindrome cost
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for p in range(1, k + 1):
                for j in range(p - 1, i):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])

        return dp[n][k]


# ---------------------------------------------------------
# Problem: Palindrome Partitioning IV (LeetCode 1745, Medium)
# Link: https://leetcode.com/problems/palindrome-partitioning-iv/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def checkPartitioning(self, s: str) -> bool:
        """
        DP + Palindrome preprocessing:
        Check if string can be split into 3 palindromic substrings.
        """
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n):
            is_pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if is_pal[0][i] and is_pal[i + 1][j] and is_pal[j + 1][n - 1]:
                    return True

        return False


# ---------------------------------------------------------
# Problem: Minimum Cost to Make at Least One Valid Path in a Grid (LeetCode 1368, Hard)
# Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# ---------------------------------------------------------
class SolutionProblemThree:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        0-1 BFS on grid graph:
        - Cost 0 if following arrow
        - Cost 1 otherwise
        """
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0)])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while dq:
            r, c = dq.popleft()
            for i, (dr, dc) in enumerate(directions, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cost = 0 if grid[r][c] == i else 1
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().palindromePartition("aabbc", 3))
    print("Problem Two Example:",
          SolutionProblemTwo().checkPartitioning("abcbdd"))
    print("Problem Three Example:",
          SolutionProblemThree().minCost([[1,1,3],[3,2,2],[1,1,4]]))
