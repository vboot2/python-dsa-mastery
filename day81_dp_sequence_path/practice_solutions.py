"""
Day 81: DP Sequence/Path - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Unique Binary Search Trees (LeetCode 96, Medium)
# Link: https://leetcode.com/problems/unique-binary-search-trees/
# ---------------------------------------------------------
class SolutionUniqueBST:
    def numTrees(self, n: int) -> int:
        """
        Catalan DP:
        dp[i] = sum(dp[left] * dp[right]) over all roots.
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += dp[root - 1] * dp[nodes - root]
            dp[nodes] = total

        return dp[n]


# ---------------------------------------------------------
# Problem 2: Out of Boundary Paths (LeetCode 576, Medium)
# Link: https://leetcode.com/problems/out-of-boundary-paths/
# ---------------------------------------------------------
class SolutionOutOfBoundary:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for _ in range(maxMove):
            next_dp = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    ways = dp[r][c]

                    # exits
                    if r == 0: result += ways
                    if r == m-1: result += ways
                    if c == 0: result += ways
                    if c == n-1: result += ways

                    # internal moves
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < m and 0 <= cc < n:
                            next_dp[rr][cc] = (next_dp[rr][cc] + ways) % MOD

            dp = next_dp

        return result % MOD


# ---------------------------------------------------------
# Problem 3: Delete and Earn (LeetCode 740, Medium)
# Link: https://leetcode.com/problems/delete-and-earn/
# ---------------------------------------------------------
class SolutionDeleteAndEarn:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Reduce to House Robber:
        value[x] = sum of all x's.
        Can't take x and x-1 together.
        """
        if not nums:
            return 0

        from collections import Counter
        count = Counter(nums)
        max_val = max(nums)

        earn = [0] * (max_val + 1)
        for v, c in count.items():
            earn[v] = v * c

        # classic house robber DP
        take, skip = 0, 0
        for v in earn:
            take, skip = skip + v, max(skip, take)

        return max(take, skip)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Unique BSTs:", SolutionUniqueBST().numTrees(3))
    print("Out of Boundary Paths:", SolutionOutOfBoundary().findPaths(2, 2, 2, 0, 0))
    print("Delete and Earn:", SolutionDeleteAndEarn().deleteAndEarn([3,4,2]))
