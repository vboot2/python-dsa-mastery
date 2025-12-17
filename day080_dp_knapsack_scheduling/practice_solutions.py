"""
Day 80: DP Knapsack/Subset + Hard Scheduling
"""

# ---------------------------------------------------------
# Problem 1: Ones and Zeroes (LeetCode 474, Medium)
# Link: https://leetcode.com/problems/ones-and-zeroes/
# ---------------------------------------------------------
class SolutionOnesAndZeroes:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        2D knapsack:
        dp[i][j] = max number of strings using <= i zeros and <= j ones.
        """
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[m][n]


# ---------------------------------------------------------
# Problem 2: Last Stone Weight II (LeetCode 1049, Medium)
# Link: https://leetcode.com/problems/last-stone-weight-ii/
# ---------------------------------------------------------
class SolutionLastStoneWeight:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Partition stones into 2 groups with minimal |sum1 - sum2|.
        Equivalent to subset sum closest to total/2.
        """
        total = sum(stones)
        target = total // 2

        dp = {0}

        for s in stones:
            new_dp = set()
            for x in dp:
                new_dp.add(x)
                new_dp.add(x + s)
            dp = new_dp

        best = max(x for x in dp if x <= target)
        return total - 2 * best


# ---------------------------------------------------------
# Problem 3: Maximum Profit in Job Scheduling (LeetCode 1235, Hard)
# Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# ---------------------------------------------------------
class SolutionJobScheduling:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        import bisect

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        ends = [j[1] for j in jobs]

        # dp[i] = max profit using first i jobs
        dp = [0] * (n + 1)

        def find_prev(i):
            s = jobs[i][0]
            return bisect.bisect_right(ends, s) - 1

        for i in range(1, n + 1):
            s, e, p = jobs[i-1]
            j = find_prev(i-1)

            dp[i] = max(dp[i-1], dp[j+1] + p)

        return dp[n]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Ones and Zeroes:", SolutionOnesAndZeroes().findMaxForm(["10","0","1"], 1, 1))
    print("Last Stone Weight II:", SolutionLastStoneWeight().lastStoneWeightII([2,7,4,1,8,1]))
    print("Job Scheduling:", SolutionJobScheduling().jobScheduling(
        [1,2,3,3], [3,4,5,6], [50,10,40,70]
    ))
