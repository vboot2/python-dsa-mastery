"""
Day 105: DP/Greedy/BFS - LeetCode Problem Solutions
"""

from typing import List
from collections import deque


# ---------------------------------------------------------
# Problem: Super Egg Drop (LeetCode 887, Hard)
# Link: https://leetcode.com/problems/super-egg-drop/
# ---------------------------------------------------------
class SolutionProblemOne:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        DP Optimization:
        dp[m][e] = max floors that can be checked with m moves and e eggs

        Recurrence:
        dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1
        """
        dp = [0] * (k + 1)
        moves = 0

        while dp[k] < n:
            moves += 1
            for e in range(k, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1

        return moves


# ---------------------------------------------------------
# Problem: Max Chunks To Make Sorted II (LeetCode 768, Hard)
# Link: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Greedy:
        - Maintain prefix max
        - Maintain suffix min
        - Cut chunk when prefix_max <= suffix_min
        """
        n = len(arr)
        prefix_max = [0] * n
        suffix_min = [0] * n

        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        chunks = 1
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                chunks += 1

        return chunks


# ---------------------------------------------------------
# Problem: Sliding Puzzle (LeetCode 773, Hard)
# Link: https://leetcode.com/problems/sliding-puzzle/
# ---------------------------------------------------------
class SolutionProblemThree:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        BFS:
        - Treat board as string state
        - BFS to reach target state
        """
        start = "".join(str(c) for row in board for c in row)
        target = "123450"

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque([(start, 0)])
        visited = {start}

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps

            idx = state.index('0')
            for nidx in neighbors[idx]:
                arr = list(state)
                arr[idx], arr[nidx] = arr[nidx], arr[idx]
                nxt = "".join(arr)

                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().superEggDrop(2, 6))
    print("Problem Two Example:", SolutionProblemTwo().maxChunksToSorted([2,1,3,4,4]))
    print("Problem Three Example:", SolutionProblemThree().slidingPuzzle([[1,2,3],[4,0,5]]))
