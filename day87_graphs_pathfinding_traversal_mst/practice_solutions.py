""" Day 87: Graphs - Pathfinding / Traversal / MST - LeetCode Problem Solutions """

from heapq import heappush, heappop
from collections import defaultdict

# ---------------------------------------------------------
# Problem: Path with Maximum Probability (LeetCode 1514, Medium)
# Link: https://leetcode.com/problems/path-with-maximum-probability/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, n, edges, succProb, start_node, end_node):
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # Max-heap for maximizing product probability
        pq = [(-1.0, start_node)]  # store negative (max-heap)
        best = {node: 0 for node in range(n)}
        best[start_node] = 1.0

        while pq:
            prob, node = heappop(pq)
            prob = -prob

            if node == end_node:
                return prob

            for nei, p in graph[node]:
                new_prob = prob * p
                if new_prob > best[nei]:
                    best[nei] = new_prob
                    heappush(pq, (-new_prob, nei))

        return 0.0


# ---------------------------------------------------------
# Problem: Redundant Connection II (LeetCode 685, Hard)
# Link: https://leetcode.com/problems/redundant-connection-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, edges):
        # Case with a node having two parents
        parent = {}
        cand1 = cand2 = None
        
        # First pass - find if there's a node with two parents
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]  # first edge to v
                cand2 = [u, v]          # second edge to v
                break
            parent[v] = u

        # Find the maximum node value to initialize Union-Find properly
        max_node = 0
        for u, v in edges:
            max_node = max(max_node, u, v)
        
        # Union-Find setup - size based on maximum node value
        uf_parent = list(range(max_node + 1))

        def find(x):
            if uf_parent[x] != x:
                uf_parent[x] = find(uf_parent[x])
            return uf_parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            uf_parent[pb] = pa
            return True

        # If found a node with two parents, temporarily remove the second candidate
        if cand2:
            temp_edges = [edge for edge in edges if edge != cand2]
        else:
            temp_edges = edges

        # Detect cycle with the modified edges
        for u, v in temp_edges:
            if not union(u, v):
                # If we find a cycle
                if cand1:
                    return cand1  # cand1 is the problematic edge
                return [u, v]     # no candidate case, return current edge

        # If no cycle found with cand2 removed, then cand2 is the redundant one
        return cand2


# ---------------------------------------------------------
# Problem: Swim in Rising Water (LeetCode 778, Hard)
# Link: https://leetcode.com/problems/swim-in-rising-water/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, grid):
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]  # (max elevation encountered, r, c)
        visited = set([(0, 0)])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            cost, r, c = heappop(pq)
            if r == n - 1 and c == n - 1:
                return cost

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heappush(pq, (max(cost, grid[nr][nc]), nr, nc))

        return -1  # never happens


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", 
          SolutionProblemOne().solve(
              3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))

    print("Problem Two Example:", 
          SolutionProblemTwo().solve([[1,2],[1,3],[2,3]]))

    print("Problem Three Example:",
          SolutionProblemThree().solve([[0,2],[1,3]]))
