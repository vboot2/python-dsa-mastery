"""
Day 101: Graph / Greedy - LeetCode Problem Solutions
"""
from typing import List
import heapq

# ---------------------------------------------------------
# Problem: Couples Holding Hands (LeetCode 765, Hard)
# Link: https://leetcode.com/problems/couples-holding-hands/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, row: List[int]) -> int:
        """
        Union-Find solution: each couple forms a node,
        unions form connected components, swaps = n - components.
        """
        n = len(row) // 2
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for i in range(0, len(row), 2):
            a, b = row[i] // 2, row[i + 1] // 2
            union(a, b)

        components = len({find(i) for i in range(n)})
        return n - components


# ---------------------------------------------------------
# Problem: Cracking the Safe (LeetCode 753, Hard)
# Link: https://leetcode.com/problems/cracking-the-safe/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, n: int, k: int) -> str:
        """
        Use DFS to construct de Bruijn sequence ensuring each
        k-length password appears exactly once.
        """
        seen = set()
        res = []

        def dfs(node):
            for x in map(str, range(k)):
                edge = node + x
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    res.append(x)

        dfs("0" * (n - 1))
        return "".join(res) + "0" * (n - 1)


# ---------------------------------------------------------
# Problem: Course Schedule III (LeetCode 630, Hard)
# Link: https://leetcode.com/problems/course-schedule-iii/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, courses: List[List[int]]) -> int:
        """
        Greedy with max heap:
        Sort by deadline, add durations, and drop longest if time exceeds deadline.
        """
        courses.sort(key=lambda x: x[1])
        total_time = 0
        max_heap = []

        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            if total_time > last_day:
                total_time += heapq.heappop(max_heap)  # remove longest course

        return len(max_heap)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve([0, 2, 1, 3]))
    print("Problem Two Example:", SolutionProblemTwo().solve(2, 2))
    print("Problem Three Example:", SolutionProblemThree().solve([[100,200],[200,1300],[1000,1250],[2000,3200]]))
