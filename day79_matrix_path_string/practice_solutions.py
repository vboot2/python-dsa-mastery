"""
Day 79: Matrix/Path + String DP - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Dungeon Game (LeetCode 174, Hard)
# Link: https://leetcode.com/problems/dungeon-game/
# ---------------------------------------------------------
class SolutionDungeonGame:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j] = min health needed at cell (i, j)
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1  # base: need at least 1 health at princess cell

        # bottom-up
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need

        return dp[0][0]


# ---------------------------------------------------------
# Problem 2: Minimum Cost for Tickets (LeetCode 983, Medium)
# Link: https://leetcode.com/problems/minimum-cost-for-tickets/
# ---------------------------------------------------------
class SolutionMinCostTickets:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dayset = set(days)
        last_day = days[-1]

        dp = [0] * (last_day + 1)

        for d in range(1, last_day + 1):
            if d not in dayset:
                dp[d] = dp[d-1]  # no travel needed
            else:
                dp[d] = min(
                    dp[d-1] + costs[0],                      # 1-day pass
                    dp[max(0, d-7)] + costs[1],              # 7-day pass
                    dp[max(0, d-30)] + costs[2]              # 30-day pass
                )
        return dp[last_day]


# ---------------------------------------------------------
# Problem 3: Minimum ASCII Delete Sum (LeetCode 712, Medium)
# Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# ---------------------------------------------------------
class SolutionMinDeleteSum:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )
        return dp[m][n]


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Dungeon Game:", SolutionDungeonGame().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print("Min Cost Tickets:", SolutionMinCostTickets().mincostTickets([1,4,6,7,8,20],[2,7,15]))
    print("Minimum Delete Sum:", SolutionMinDeleteSum().minimumDeleteSum("delete", "leet"))
