"""
Day 107: DP/Linked List - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Guess Number Higher or Lower II (LeetCode 375, Medium)
# Link: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# ---------------------------------------------------------
class SolutionProblemOne:
    def getMoneyAmount(self, n: int) -> int:
        """
        DP (Minimax):
        dp[l][r] = min over k in [l, r] of k + max(dp[l][k-1], dp[k+1][r])
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                dp[l][r] = float('inf')
                for k in range(l, r):
                    dp[l][r] = min(dp[l][r], k + max(dp[l][k - 1], dp[k + 1][r]))

        return dp[1][n]


# ---------------------------------------------------------
# Problem: Stone Game III (LeetCode 1406, Hard)
# Link: https://leetcode.com/problems/stone-game-iii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        DP:
        dp[i] = max score difference current player can achieve starting at i.
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"


# ---------------------------------------------------------
# Problem: Design Linked List (LeetCode 707, Medium)
# Link: https://leetcode.com/problems/design-linked-list/
# ---------------------------------------------------------
class SolutionProblemThree:
    """
    Singly linked list implementation with:
    - get
    - addAtHead
    - addAtTail
    - addAtIndex
    - deleteAtIndex
    """
    class Node:
        def __init__(self, val=0, nxt=None):
            self.val = val
            self.next = nxt

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.head = self.Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = self.Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = self.Node(val, cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().getMoneyAmount(5))
    print("Problem Two Example:", SolutionProblemTwo().stoneGameIII([1,2,3,7]))

    ll = SolutionProblemThree()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    print("Problem Three Example:", ll.get(1))
