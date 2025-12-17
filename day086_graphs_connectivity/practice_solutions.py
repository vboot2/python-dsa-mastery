""" Day 86: Graphs Connectivity - LeetCode Problem Solutions """

from collections import defaultdict, deque

# ---------------------------------------------------------
# Problem: Find if Path Exists in Graph (LeetCode 1971, Easy)
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, n, edges, source, destination):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to check connectivity
        q = deque([source])
        visited = set([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return False


# ---------------------------------------------------------
# Problem: Minimum Height Trees (LeetCode 310, Medium)
# Link: https://leetcode.com/problems/minimum-height-trees/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, n, edges):
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initialize leaf queue
        leaves = deque([i for i in range(n) if degree[i] == 1])

        remaining = n
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

        return list(leaves)


# ---------------------------------------------------------
# Problem: Number of Operations to Make Network Connected (LeetCode 1319, Medium)
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, n, connections):
        if len(connections) < n - 1:
            return -1  # Not enough edges

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        # Build union-find
        for u, v in connections:
            union(u, v)

        # Count connected components
        components = len({find(i) for i in range(n)})
        return components - 1  # operations needed


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", 
          SolutionProblemOne().solve(3, [[0,1],[1,2]], 0, 2))

    print("Problem Two Example:", 
          SolutionProblemTwo().solve(4, [[1,0],[1,2],[1,3]]))

    print("Problem Three Example:", 
          SolutionProblemThree().solve(4, [[0,1],[0,2],[1,2]]))
