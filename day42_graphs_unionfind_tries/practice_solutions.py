"""
Day 42: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""
from collections import deque

# ---------------------------------------------------------
# Problem 1: Possible Bipartition (LeetCode 886, Medium)
# Link: https://leetcode.com/problems/possible-bipartition/
# ---------------------------------------------------------
class SolutionPossibleBipartition:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}
        for node in range(1, n + 1):
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        if nei not in color:
                            color[nei] = 1 - color[curr]
                            queue.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True


# ---------------------------------------------------------
# Problem 2: Minimize Malware Spread (LeetCode 924, Hard)
# Link: https://leetcode.com/problems/minimize-malware-spread/
# ---------------------------------------------------------
class SolutionMinMalwareSpread:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        n = len(graph)
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if size[rootX] >= size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]

        # Build connected components
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    union(i, j)

        # Count infections per component
        infected_count = {}
        for node in initial:
            root = find(node)
            infected_count[root] = infected_count.get(root, 0) + 1

        # Choose node whose removal minimizes infection
        result = (-1, float('inf'))
        for node in sorted(initial):
            root = find(node)
            if infected_count[root] == 1:
                if size[root] > result[0]:
                    result = (size[root], node)
        return result[1] if result[0] != -1 else min(initial)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Possible Bipartition:",
          SolutionPossibleBipartition().possibleBipartition(4, [[1,2],[1,3],[2,4]]))

    graph = [[1,1,0],[1,1,0],[0,0,1]]
    initial = [0,1]
    print("Minimize Malware Spread:",
          SolutionMinMalwareSpread().minMalwareSpread(graph, initial))
