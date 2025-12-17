"""
Day 41: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""
from collections import defaultdict, deque

# ---------------------------------------------------------
# Problem 1: Longest Consecutive Sequence (LeetCode 128, Medium)
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# ---------------------------------------------------------
class SolutionLongestConsecutive:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:      # start of sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


# ---------------------------------------------------------
# Problem 2: Evaluate Division (LeetCode 399, Medium)
# Link: https://leetcode.com/problems/evaluate-division/
# ---------------------------------------------------------
class SolutionEvaluateDivision:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build the bidirectional weighted graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set([start])

            while queue:
                node, val = queue.popleft()
                if node == end:
                    return val
                for nei, weight in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, val * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Longest Consecutive Sequence:",
          SolutionLongestConsecutive().longestConsecutive([100,4,200,1,3,2]))
    
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print("Evaluate Division:",
          SolutionEvaluateDivision().calcEquation(equations, values, queries))
