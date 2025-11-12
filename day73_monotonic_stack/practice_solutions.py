"""
Day 73: Monotonic Stack - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem 1: Daily Temperatures (LeetCode 739, Medium)
# Link: https://leetcode.com/problems/daily-temperatures/
# ---------------------------------------------------------
class SolutionDailyTemperatures:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []  # stores indices
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


# ---------------------------------------------------------
# Problem 2: Online Stock Span (LeetCode 901, Medium)
# Link: https://leetcode.com/problems/online-stock-span/
# ---------------------------------------------------------
class StockSpanner:
    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# ---------------------------------------------------------
# Problem 3: Next Greater Element II (LeetCode 503, Medium)
# Link: https://leetcode.com/problems/next-greater-element-ii/
# ---------------------------------------------------------
class SolutionNextGreaterII:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # store indices

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Daily Temperatures:",
        SolutionDailyTemperatures().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
    )
    spanner = StockSpanner()
    print(
        "Stock Spanner Example:",
        [spanner.next(p) for p in [100, 80, 60, 70, 60, 75, 85]],
    )
    print(
        "Next Greater Element II:",
        SolutionNextGreaterII().nextGreaterElements([1, 2, 1]),
    )
