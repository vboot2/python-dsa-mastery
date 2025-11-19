"""
Day 80: DP Knapsack/Subset + Hard Scheduling
Knapsack/Subset DP solves problems involving capacity constraints.
Scheduling DP focuses on selecting non-overlapping jobs to maximize profit.
"""

# ---------------------------------------------------------
# Example 1: 0/1 Knapsack (Classic Form)
# ---------------------------------------------------------

def example_one(weights, values, capacity):
    """
    Basic 0/1 knapsack DP:
    dp[c] = max value achievable with capacity c.
    """
    dp = [0] * (capacity + 1)

    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)

    return dp[capacity]

print("Output Example 1:", example_one([1,2,3], [6,10,12], 5))


# ---------------------------------------------------------
# Example 2: Weighted Interval Scheduling (DP + Binary Search)
# ---------------------------------------------------------

def example_two(jobs):
    # sort by end time
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)

    # p[i] = latest job ending before job i starts
    import bisect
    ends = [job[1] for job in jobs]

    def find_prev(i):
        s = jobs[i][0]
        return bisect.bisect_right(ends, s) - 1

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        _, _, profit = jobs[i-1]
        j = find_prev(i-1)

        # choose or skip job i-1
        dp[i] = max(dp[i-1], dp[j+1] + profit)

    return dp[n]

print("Output Example 2:", example_two([(1,3,50),(3,5,20),(6,19,100),(2,100,200)]))
