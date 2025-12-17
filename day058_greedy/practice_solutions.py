"""
Day 58: Greedy - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Task Scheduler (LeetCode 621, Medium)
# Link: https://leetcode.com/problems/task-scheduler/
# ---------------------------------------------------------
from collections import Counter


class SolutionTaskScheduler:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_freq)
        result = max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
        return result


# ---------------------------------------------------------
# Problem: Two City Scheduling (LeetCode 1029, Medium)
# Link: https://leetcode.com/problems/two-city-scheduling/
# ---------------------------------------------------------
class SolutionTwoCityScheduling:
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0

        for i in range(n):
            total += costs[i][0]
        for i in range(n, 2 * n):
            total += costs[i][1]
        return total


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Problem 621 Example:",
        SolutionTaskScheduler().leastInterval(["A", "A", "A", "B", "B", "B"], 2),
    )
    print(
        "Problem 1029 Example:",
        SolutionTwoCityScheduling().twoCitySchedCost(
            [[10, 20], [30, 200], [400, 50], [30, 20]]
        ),
    )
