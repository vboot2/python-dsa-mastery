"""
Day 11: Deques Practice Solutions
"""

from collections import deque
from typing import List

# ---------------------------------------------------------
# Problem: Implement Stack using Queues (LeetCode 225)
# Link: https://leetcode.com/problems/implement-stack-using-queues/
# ---------------------------------------------------------
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # rotate so new element is at front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# ---------------------------------------------------------
# Problem: Design Circular Deque (LeetCode 641)
# Link: https://leetcode.com/problems/moving-average-from-data-stream/
# ---------------------------------------------------------
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.q = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.q[0] if self.q else -1

    def getRear(self) -> int:
        return self.q[-1] if self.q else -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k
