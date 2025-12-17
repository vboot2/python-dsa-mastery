"""
Day 10: Queues - LeetCode Problem Solutions
"""

from collections import deque
import heapq

# ---------------------------------------------------------
# Problem: Implement Queue using Stacks (LeetCode 232, Easy)
# Link: https://leetcode.com/problems/implement-queue-using-stacks/
# ---------------------------------------------------------
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# ---------------------------------------------------------
# Problem: Number of Recent Calls (LeetCode 933, Easy)
# Link: https://leetcode.com/problems/number-of-recent-calls/
# ---------------------------------------------------------
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# ---------------------------------------------------------
# Problem: Sliding Window Maximum (LeetCode 239, Hard)
# Link: https://leetcode.com/problems/sliding-window-maximum/
# ---------------------------------------------------------
class SolutionSlidingWindowMax:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        res = []
        for i, num in enumerate(nums):
            # remove indices out of window
            if q and q[0] <= i - k:
                q.popleft()
            # maintain decreasing order
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
